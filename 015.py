# -*- coding: utf-8 -*-
# 末尾のN行を出力（確認はtailコマンド）

import sys

if __name__ == "__main__":
    args = sys.argv
    textTmp = []
    for line in open("hightemp.txt", "r"):
        textTmp.append(line)
    for oput in textTmp[len(textTmp) - int(args[1])::]:
        print(oput, end="")
