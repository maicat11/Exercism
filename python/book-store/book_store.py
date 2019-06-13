def total(basket):
    cost = 0
    if len(set(basket)) <= 1:
        cost = 800 * len(basket)
        return cost

    if len(set(basket)) == 2:
        cost = (800)