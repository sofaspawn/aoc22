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
    for r in rounds:
        [o, s] = r.split(' ') 
        print(o, s)
        if symbols[o] == symbols[s]:
            tscore += symbols[s] + 3  # Draw
        elif (symbols[o] == 1 and symbols[s] == 2) or \
             (symbols[o] == 2 and symbols[s] == 3) or \
             (symbols[o] == 3 and symbols[s] == 1):
            tscore += symbols[s] + 6  # Win
        else:
            tscore += symbols[s]  # Loss

    return tscore

print(solution())
