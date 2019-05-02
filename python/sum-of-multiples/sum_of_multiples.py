def sum_of_multiples(limit, multiples):
    return sum(set([num * i for num in multiples for i in range(1, limit) if num * i < limit]))
