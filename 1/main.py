#! /usr/bin/env python3

def solution():
    f = open('calories', 'r')
    elvesCals = f.read().split('\n\n')
    # part 1
    totalcals = []
    for elf in elvesCals:
        totalcal = 0
        totalcal += sum([int(i) for i in elf.split('\n') if i!=''])
        totalcals.append(totalcal)
    #return max(totalcals)

    # part 2
    totalcals.sort()
    return sum(totalcals[-3:])
    

print(solution())

