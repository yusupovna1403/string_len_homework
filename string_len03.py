def main(a,b):
    """
    String type variables a and b are given. Return True if the length is equal. If not equal, return False.
    Args:
        a: string
        b: string
    Returns:
        True or False
    """
    if len(a) == len(b):
        return True
    else:
        return False
print(main("code" , "exam"))
print(main("code" , "python"))
    