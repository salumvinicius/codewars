def create_phone_number(n):
    prefix = "".join(str(num) for num in n)
    return "(" + prefix[:3] + ") " + prefix[3:6] + "-" + prefix[6:]