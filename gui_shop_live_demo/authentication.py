import json
from canvas import tk
from tkinter import Button, Entry, Label
from helpers import clean_screen
from products import render_products


def login(username, password):
    with open('db/user_credentials_db.txt', 'r') as file:
        lines = file.readlines()
        for line in lines:
            user, pas = line[:-1].split(', ')
            if user == username and pas == password:
                with open('db/current_user.txt', 'w') as current_user_file:
                    current_user_file.write(username)
                render_products()
                return
            else:
                render_login(errors=True)


def register(**user):
    user.update({'products': []})

    with open('db/users.txt', 'a') as file:
        file.write(json.dumps(user))
        file.write('\n')

    with open('db/user_credentials_db.txt', 'a') as file:
        file.write(f'{user.get("username")}, {user.get("password")}')
        file.write('\n')


def render_register():
    clean_screen()
    Label(text='Enter your username:').grid(row=0, column=0)
    username = Entry(tk)
    username.grid(row=0, column=1)
    Label(text='Enter your password:').grid(row=1, column=0)
    password = Entry(tk, show='*')
    password.grid(row=1, column=1)
    Label(text='Enter your firstname:').grid(row=2, column=0)
    firstname = Entry(tk)
    firstname.grid(row=2, column=1)
    Label(text='Enter your lastname:').grid(row=3, column=0)
    lastname = Entry(tk)
    lastname.grid(row=3, column=1)
    Button(tk, text='Register', bg='green',
           command=lambda: register(username=username.get(), password=password.get(), firstname=firstname.get(),
                                    lastname=lastname.get())).grid(row=4, column=0)


def render_login(errors=None):
    clean_screen()
    Label(text='Enter your username:').grid(row=0, column=0)
    username = Entry(tk)
    username.grid(row=0, column=1)
    Label(text='Enter your password:').grid(row=1, column=0)
    password = Entry(tk, show='*')
    password.grid(row=1, column=1)
    Button(tk, text='Enter', bg='green', command=lambda: login(username=username.get(), password=password.get())).grid(
        row=2, column=0)
    if errors:
        Label(text='Invalid username or password.').grid(row=3, column=0)


def render_main_enter_screen():
    Button(tk, text='Login', bg='green', fg='white', command=render_login).grid(row=0, column=0)
    Button(tk, text='Register', bg='yellow', command=render_register).grid(row=0, column=1)