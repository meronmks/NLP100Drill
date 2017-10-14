# -*- coding: utf-8 -*-
# 先頭からN行を出力（確認はheadコマンド）

import sys

if __name__ == "__main__":
    args = sys.argv
    count = 0
    for line in open("hightemp.txt", "r"):
        if count == int(args[1]):
            break
        print(line, end="")
        count += 1
