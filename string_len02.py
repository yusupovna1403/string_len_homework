def main(a):
    """
    A string type variable is given. Return True if its length is even. Return False if its length is odd.
    Args:
        a: string
    Returns:
        True or False
    """
    length = len(a)
    if length % 2 == 0:
        return True
    else:
        return False
print(main("code"))