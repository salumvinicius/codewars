def replace_exclamation(st):
    sem_vogal = ""
    for x in st:
        if x in "aeiouAEIOU":
            sem_vogal += "!"
        else:
            sem_vogal += x
    return sem_vogal
​
print(replace_exclamation("Hi!"))
print(replace_exclamation("!Hi! Hi!"))
print(replace_exclamation("aeiou"))
print(replace_exclamation("ABCDE"))