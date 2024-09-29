#! /usr/bin/env python3

def solution():
    symbolspt1 = {
        'A': 1,
        'B': 2,
        'C': 3,
        'X': 1,
        'Y': 2,
        'Z': 3,
    }
    symbolspt2 = {
        'A': 1, #scissors
        'B': 2, #paper
        'C': 3, #rock
        'X': 0, #lose
        'Y': 3, #draw
        'Z': 6, #win
    }
    rounds = open('strategy', 'r').read().strip().split('\n')
    tscore = 0 
    # part 1
    '''
    for r in rounds:
        [o, s] = r.split(' ') 
        if symbolspt1[o] == symbolspt1[s]:
            tscore += symbolspt1[s] + 3  # Draw
        elif (symbolspt1[o] == 1 and symbolspt1[s] == 2) or \
             (symbolspt1[o] == 2 and symbolspt1[s] == 3) or \
             (symbolspt1[o] == 3 and symbolspt1[s] == 1):
            tscore += symbolspt1[s] + 6  # Win
        else:
            tscore += symbolspt1[s]  # Loss
    '''
    # part 2
    for r in rounds:
        [o, s] = r.split(' ') 
        print(o, s)
        for i in symbolspt2:

    return tscore

print(solution())
