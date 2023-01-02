def main(s):
    """
    Given variable type string s. Return the character in the middle.
    If the length is even, return two characters in the middle.

    Args:
        s: str
    Returns:
        str: answer
    """
    a = len(s)
    if a > 2:
        if a % 2 == 1:
            return s[a // 2]
        else:
            return s[a//2 - 1] + s[a//2]
    else:
        return "Please enter text longer than 2"
print(main("coder"))
print(main("code"))
print(main("cd"))