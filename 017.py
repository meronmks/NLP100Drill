# -*- coding: utf-8 -*-
# １列目の文字列の異なり（確認にはsort, uniqコマンド）

if __name__ == "__main__":
    stringList = []
    for line in open("hightemp.txt", "r"):
        splitLine = line.split()
        if splitLine[0] not in stringList:
            stringList.append(splitLine[0])
    wfile = open("uniq.txt", "w")
    for line in stringList:
        wfile.write(line + "\n")
    wfile.close()
