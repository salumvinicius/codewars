def likes(names):
    if len(names) == 0:
        return "no one likes this"
    if len(names) == 1:
        return names[0] + ' likes this'
    if len(names) <= 3:
        return ", ".join(names[:-1]) + " and " + names[-1] + " like this"
    else:
        return ", ".join(names[:2]) + " and " + str(len(names[2:])) + " others like this"