def char_position(text):
    if not isinstance(text, str): return 'Please input string'
    position_dict = {}
    for i, char in enumerate(text):
        if char not in position_dict:
            position_dict[char] = set()
        position_dict[char].add(i)

    return position_dict
    
text = 'Hello'

print(char_position(text))