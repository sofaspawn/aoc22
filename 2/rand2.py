#! /usr/bin/env python3

ss = ['()', '()[]{}', '(]','([])']

def solution():
    matches = {
        "(":")",
        "{":"}",
        "[":"]",
        "]":"[",
        ")":"(",
        "}":"{",
    } 
    stack = []
    for e in s:
        if e not in stack:
            stack.append(e)

for s in ss:
    print(solution(s))
