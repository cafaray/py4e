def no_duplicates(str_):
    """ Determine if str_ has all unique characters """
    print(set(str_))
    return len(str_) == len(set(str_))

print(no_duplicates('abccdefg'))