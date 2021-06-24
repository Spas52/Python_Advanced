import os


def create_file(file_path):
    file = open(file_path, 'w')
    file.close()
    return file


def add_file_content(file_path, content):
    with open(file_path, 'a') as file:
        file.write(content + '\n')
    return file


def replace_file_string(file_path, old_string, new_string):
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            data = file.read()
            data = data.replace(old_string, new_string)
        with open(file_path, 'w') as file:
            file.write(data)
    else:
        print('An error occurred')


def delete_file(file_path):
    try:
        os.remove(file_path)
    except FileNotFoundError:
        print('An error occurred')


input_data = input()

while not input_data == "End":
    input_data = input_data.split('-')
    command = input_data[0]

    if command == 'Create':
        file_path = input_data[1]
        create_file(file_path)
    elif command == 'Add':
        file_path = input_data[1]
        content = input_data[2]
        add_file_content(file_path, content)
    elif command == 'Replace':
        file_path = input_data[1]
        old_string = input_data[2]
        new_string = input_data[3]
        replace_file_string(file_path, old_string, new_string)
    elif command == 'Delete':
        file_path = input_data[1]
        delete_file(file_path)
    input_data = input()



