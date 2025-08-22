def validate_pin(pin):
    wrong = 0
    numbers = "0123456789"
    for i in pin:
        if i not in numbers:
            wrong += 1
    
    return True if len(pin) == 4 and wrong == 0 or len(pin) == 6 and wrong == 0 else False