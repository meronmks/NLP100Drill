# -*- coding: utf-8 -*-
# 各行を3コラム目の数値の降順にソート（確認にはsortコマンド）
# sort -k4r hightemp.txtでも大丈夫だが数値でとあるので
# sort -k4nr hightemp.txtの方がいい？

import sys
import datetime
from operator import itemgetter

if __name__ == "__main__":
    args = sys.argv
    textTmp = []
    for line in open("hightemp.txt", "r"):
        textTmp.append(line.split())
    textTmp.sort(key=itemgetter(3))
    for line in textTmp[::-1]:
        for text in line:
            print(text + "	", end="")
        print()
