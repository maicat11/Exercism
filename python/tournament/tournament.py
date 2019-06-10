from collections import defaultdict

def tally(tournament_results):
    results_keeper = {}

    for game in tournament_results:
        r = game.split(';')
        result = r[2]
        for team in r[:2]:
            if team not in results_keeper.keys():
                results_keeper[team] = defaultdict(int)
            results_keeper[team]['MP'] += 1

        if result == 'win':
            results_keeper[r[0]]['W'] += 1
            results_keeper[r[0]]['D'] += 0
            results_keeper[r[0]]['L'] += 0
            results_keeper[r[0]]['P'] += 3
            results_keeper[r[1]]['W'] += 0
            results_keeper[r[1]]['D'] += 0
            results_keeper[r[1]]['L'] += 1
            results_keeper[r[1]]['P'] += 0
        elif r[2] == 'loss':
            results_keeper[r[1]]['W'] += 1
            results_keeper[r[1]]['D'] += 0
            results_keeper[r[1]]['L'] += 0
            results_keeper[r[1]]['P'] += 3
            results_keeper[r[0]]['W'] += 0
            results_keeper[r[0]]['D'] += 0
            results_keeper[r[0]]['L'] += 1
            results_keeper[r[0]]['P'] += 0
        else:
            results_keeper[r[0]]['W'] += 0
            results_keeper[r[0]]['D'] += 1
            results_keeper[r[0]]['L'] += 0
            results_keeper[r[0]]['P'] += 1
            results_keeper[r[1]]['W'] += 0
            results_keeper[r[1]]['D'] += 1
            results_keeper[r[1]]['L'] += 0
            results_keeper[r[1]]['P'] += 1

    table = [['Team', 'MP', 'W', 'D', 'L','P']]

    for team, results in results_keeper.items():
        table.append([team] + list(results.values()))

    points = table[1:]
    points.sort(key=lambda x: (-x[5], x[0]))   # sort by points
    table[1:] = points                         # reassign sorted back to table
    stringify = (['{:<30} | {:>2} | {:>2} | {:>2} | {:>2} | {:>2}'
                      .format(x[0], x[1], x[2], x[3], x[4], x[5]) for x in table])

    return stringify