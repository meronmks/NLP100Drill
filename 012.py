# -*- coding: utf-8 -*-
# 1列目をcol1.txtに，2列目をcol2.txtに保存（確認はcutコマンド）

if __name__ == "__main__":
    col1 = open("col1.txt", "w")
    col2 = open("col2.txt", "w")
    for line in open("hightemp.txt", "r"):
        split = line.split()
        col1.write(split[0] + "\n")
        col2.write(split[1] + "\n")
    col1.close()
    col2.close()
