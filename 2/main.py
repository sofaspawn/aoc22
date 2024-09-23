#! /usr/bin/env python3

def solution():
    # part 1
    symbols = {
        'A': 1,
        'B': 2,
        'C': 3,
        'X': 1,
        'Y': 2,
        'Z': 3,
    }
    rounds = open('strategy', 'r').read().strip().split('\n')
    tscore = 0 
    exp = [
        'A Y',
        'B X',
        'C Z'
        ]
    for r in rounds:
        [o, s] = r.split(' ') 
        print(o, s)
        if symbols[o]<symbols[s]:
            tscore += symbols[s] + 6
        elif symbols[o]==symbols[s]:
            tscore += symbols[s] + 3
        elif symbols[o] > symbols[s]:
            tscore += symbols[s]

    return tscore

print(solution())
