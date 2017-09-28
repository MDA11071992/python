def hotel_cost(nights):
    return 140 * nights


def plane_ride_cost(city):
    if city == "Charlotte":
        return 183
    elif city == "Tampa":
        return 220
    elif city == "Pittsburgh":
        return 222
    elif city == "Los Angeles":
        return 475
    else:
        return 0


def rental_car_cost(days):
    costs = 40 * days
    if days >= 7:
        costs -= 50
    elif days >= 3:
        costs -= 20
    return costs


def trip_cost(city, days, spending_money):
    return hotel_cost(days) + rental_car_cost(days) + plane_ride_cost(city) + spending_money


cost = trip_cost(city=str(input('city: ')), days=int(input('days: ')),
                 spending_money=int(input('spending money: ')))
print("%s %d%s" % ('costs:', cost, '$'))
