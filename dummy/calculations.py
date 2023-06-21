def sum(a,b):
    if not isinstance(a, (int, float))  or not isinstance(b, (int, float)):
        return 'Provide int or float values'
    
    return a + b

