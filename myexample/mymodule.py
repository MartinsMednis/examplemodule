def the_function(param1, param2):
    """This is an example of Google style.

Args:
    param1: This is the first param.
    param2: This is a second param.

Returns:
    This is a description of what is returned.

Raises:
    KeyError: Raises an exception when param1 is 1000."""
    if param1 == 1000:
        raise Exception("Oh no")
    return 4

if __name__ == "__main__":
    numpy_v_lists()
