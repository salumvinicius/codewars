def is_palindrome(s):
    x = s.upper()
    if x == x[::-1]:
        return True
    else:
        return False
​