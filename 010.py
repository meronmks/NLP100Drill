# -*- coding: utf-8 -*-
# 行数のカウント（確認はwcで）

if __name__ == "__main__":
    lineCounter = 0
    for line in open("hightemp.txt", "r"):
        lineCounter += 1
    print("lineCount : " + str(lineCounter))
