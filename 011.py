# -*- coding: utf-8 -*-
# タブをスペースに置換（確認はsedコマンド，trコマンド，もしくはexpandコマンド）

if __name__ == "__main__":
    writeFile = open("tab2SpaceConv.txt", "w")
    for line in open("hightemp.txt", "r"):
        writeFile.write(line.replace("	", " "))
    writeFile.close()
