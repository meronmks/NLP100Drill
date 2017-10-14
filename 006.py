# -*- coding: utf-8 -*-
# 集合

def nGram(inStr, n):
    l = len(inStr)
    wl = []
    for i in range(l):
        wl.append(inStr[i:i+n])
    return wl

if __name__ == "__main__":
    str1 = "paraparaparadise"
    str2 = "paragraph"

    X = set(nGram(str1, 2))
    Y = set(nGram(str2, 2))

    print("bigram出力の集合")
    print(X)
    print(Y)

    union = X|Y
    inter = X&Y
    diff = X-Y

    print("和集合")
    print(union)
    print("積集合")
    print(inter)
    print("差集合")
    print(diff)
    print("seが含まれるか")
    XinSE = "se" in X
    YinSE = "se" in Y
    print(XinSE)
    print(YinSE)
