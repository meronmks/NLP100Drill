# -*- coding: utf-8 -*-
# 各行の1コラム目の文字列の出現頻度を求め，出現頻度の高い順に並べる（確認にはscut, uniq, sortコマンド）
# cut -f 1 hightemp.txt | sort | uniq -c | sort -nr

from collections import OrderedDict

if __name__ == "__main__":
    dic = {}
    for line in open("hightemp.txt", "r"):
        lineSplit = line.split()
        if lineSplit[0] in dic:
            dic[lineSplit[0]] += 1
        else:
            dic.update({lineSplit[0]: 1})
    sortDic = OrderedDict(
        sorted(dic.items(), key=lambda x: x[1], reverse=True))
    for sd in sortDic:
        print(sd)
