# -*- coding: utf-8 -*-
# col1.txtとcol2.txtをマージ（確認はpasteコマンド）

if __name__ == "__main__":
    mergeCol = open("mergeCol.txt", "w")
    col2 = open("col2.txt", "r")
    for line1 in open("col1.txt", "r"):
        line2 = col2.readline()
        mergeCol.write(line1.replace("\n", "") + "	" + line2)
    mergeCol.close()
    col2.close()
