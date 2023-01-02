def main(s1,s2):
    """
    Given two strings, s1 and s2. Return the shortest length between them.
    Args:
        s1: string
        s2: string
    Returns:
        shortest string
    """
    if len(s1) < len(s2):
        return s1
    else:
        return s2
print(main("code" , "python"))
print(main("code" , "exam"))
