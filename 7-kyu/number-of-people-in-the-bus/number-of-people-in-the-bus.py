def number(bus_stops):
    people_on = 0
    for i in bus_stops:
        i = i[0] - i [1]
        people_on = people_on + i
    return people_on