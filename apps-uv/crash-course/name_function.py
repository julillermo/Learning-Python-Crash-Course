def get_formatted_name_pass(first, last):
    """ Generate a neatly formatted full name. """
    full_name = f"{first} {last}"
    return full_name.title()

def get_formatted_name_fail(first, middle, last):
    """ Generate a neatly formatted full name. """
    full_name = f"{first} {middle} {last}"
    return full_name.title()

def get_formatted_name_corrected(first, last, middle=''):
    """ Generate a neatly formatted full name. """
    if middle:
        full_name = f"{first} {middle} {last}"
    else:
        full_name = f"{first} {last}"
    return full_name.title()