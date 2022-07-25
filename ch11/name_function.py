def get_formatted_name(first, last, middle=""):
    """Generate a neatly formatted full name"""
    # Make middle name optional (move to the end param, so that test-case passes. Use 'if' condition to check
    if middle:
        full_name = f"{first} {middle} {last}"
    else:
        full_name = f"{first} {last}"
    return full_name.title()
