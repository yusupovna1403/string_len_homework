def main(s):
    """
    A string of length three is given. Check that it is a palindrome.
    Return True if the palindrome is False otherwise

    Args:
        s: str
    Returns:
        bool: answer
    """
    if len(s) == 3:
        if s[0] == s[2]:
            return True
        else:
            return False
    else:
        return "Please,enter a string of length three"
print(main("cdc"))
print(main("ccd"))
print(main("dfghj"))