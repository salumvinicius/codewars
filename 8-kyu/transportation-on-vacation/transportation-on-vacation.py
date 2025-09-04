def rental_car_cost(d):
    if 7 > d >= 3:
        return (40 * d) - 20
    if d < 3:
        return 40 * d
    else:
        return (40 * d) - 50