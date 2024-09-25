#! /usr/bin/env python3
# random program to encode and decode strings
strs = ['something is going on',
        'This is. int;;;eresting',
        'this is funny',
        'interesting challenge']

def encode(strs):
    encoded_string = ''
    for s in strs:
        for i in s:
            encoded_string+=str(ord(i))
            encoded_string+='.'
        encoded_string+=';'
    return encoded_string

def decode(s):
    strs = []
    cs = ''
    cb = ''
    i = 0
    while i<len(s):
        if s[i]==';':
            strs.append(cs)
            cs = ''
        elif s[i]=='.':
            cs+=chr(int(cb))
            cb = ''
        else:
            cb+=s[i]
        i+=1
    return strs

encoded_string = encode(strs);
strs2 = decode(encoded_string);

print(encoded_string)
print(strs2)
print(strs == strs2)
