# -*- coding: utf-8 -*-
# n-gram

def nGram(inStr, n):
    l = len(inStr)
    for i in range(l):
        print(inStr[i:i+n])

if __name__ == "__main__":
    s = raw_input(">")
    print(s)
    nGram(s.replace(" ", ""), 2)
    s = s.split()
    nGram(s, 2)
