def get_info(**kwargs):
    return f"This is {kwargs.get('name')} from {kwargs.get('town')} and he is {kwargs.get('age')} years old"


print(get_info(**{"name": "George", "town": "Sofiq", "age": "20"}))
