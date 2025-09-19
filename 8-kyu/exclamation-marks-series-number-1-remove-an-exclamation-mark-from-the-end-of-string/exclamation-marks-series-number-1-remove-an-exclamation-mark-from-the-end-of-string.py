def remove(s):
    if s == "":
        return s
    if s[-1] == "!":
        return s[:-1]
​
    else:
        return s