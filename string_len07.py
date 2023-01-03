def main(s1,s2,s3):
    """
    Given three strings, s1, s2 and s3. find their odd lengths, example "[s1, s2]". If there is no odd length, return "[]".
    Args:
        s1: string
        s2: string
        s3: string
    Returns:
        string
    """
    n1 = len(s1)
    n2 = len(s2)
    n3 = len(s3)
    list = []
    #if n1 % 2 == 1 and n2 % 2 == 1 and n3 % 2 == 1:
        #return f'[{s1},{s2},{s3}]'
    #elif n1 % 2 == 1 and n2 % 2 == 1 and n3 % 2 == 0:
        #return f'[{s1},{s2}]'
    #elif n1 % 2 == 1 and n2 % 2 == 0 and n3 % 2 == 1:
        #return f'[{s1},{s3}]'
    #elif n1 % 2 == 0 and n2 % 2 == 1 and n3 % 2 == 1:
        #return f'[{s2},{s3}]'
    #elif n1 % 2 == 1 and n2 % 2 == 0 and n3 % 2 == 0:
        #return f'[{s1}]'
    #elif n1 % 2 == 0 and n2 % 2 == 1 and n3 % 2 == 0:
        #return f'[{s2}]'
    #elif n1 % 2 == 0 and n2 % 2 == 0 and n3 % 2 == 1:
        #return f'[{s3}]'
    #else:
        #return f'[]'
    if n1 % 2 == 1:
        list.append(s1)
    if n2 % 2 == 1:
        list.append(s2)
    if n3 % 2 == 1:
        list.append(s3)
    return list
print(main("coder","code","python"))