def greet_user(name):
    if not isinstance(name, str):
        return 'Not a string value'
    name = name.strip()
    return f'Hello {name}'