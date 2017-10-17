# -*- coding: utf-8 -*-
# ファイルをN分割する（同様の処理をsplitコマンドで）
# split -l 3 hightemp.txt output

import sys

if __name__ == "__main__":
    args = sys.argv
    splitNum = args[1]
    i = 0
    j = 0
    for line in open("hightemp.txt", "r"):
        j += 1
        wfile = open("hightemp_split_" + str(i) + ".txt", "a")
        wfile.write(line)
        wfile.close()
        if j >= int(splitNum):
            i += 1
            j = 0
