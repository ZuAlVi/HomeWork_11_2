def func(value):
    """The function returns the string in uppercase"""
    return value.upper()


def title_func(value):
    """The function returns a string with capitalized all words"""
    temp_list = value.split()
    total_string = ''
    for item in temp_list:
        total_string += ' ' + ''.join(item.title())
    return total_string.strip()
