import json
import os
from canvas import tk
from helpers import clean_screen
from PIL import Image, ImageTk
from tkinter import Button, Label

base_folder = os.path.dirname(__file__)


def buy_product(button):
    _, product_id = button.cget('text').split()
    product_id = int(product_id)
    current_logged_in_user = None
    with open('db/current_user.txt', 'r') as file:
        current_logged_in_user = file.read()
    with open('db/users.txt', 'r+') as file:
        users = file.readlines()
        file.seek(0)
        for user in users:
            user_as_dict = json.loads(user)
            if user_as_dict.get('username') == current_logged_in_user:
                user_as_dict['products'].append(product_id)
            file.write(json.dumps(user_as_dict))
            file.write('\n')

    with open('db/products.txt', 'r+') as file:
        products = file.readlines()
        file.seek(0)
        for product in products:
            product_as_dict = json.loads(product)
            if product_as_dict['id'] == product_id:
                product_as_dict['count'] -= 1
            file.write(json.dumps(product_as_dict))
            file.write('\n')

    render_products()


def render_products():
    clean_screen()
    with open('db/products.txt', 'r') as file:
        products = file.readlines()
        col_counter = 0
        for product in products:
            current_product = json.loads(product)
            Label(text=current_product.get('name')).grid(row=0, column=col_counter)
            image = Image.open(os.path.join(os.path.join(base_folder, 'images'), current_product.get('img_path')))
            image = image.resize((250, 250))
            photo = ImageTk.PhotoImage(image)
            img_label = Label(image=photo)
            img_label.image = photo
            img_label.grid(row=1, column=col_counter)
            button = Button(tk, text=f'Buy {current_product.get("id")}')
            button.configure(command=lambda b=button: buy_product(b))
            button.grid(row=3, column=col_counter)
            Label(text=current_product.get('count')).grid(row=2, column=col_counter)
            col_counter += 1