# -*- coding: utf-8 -*-
# 「パトカー」＋「タクシー」＝「パタトクカシーー」

if __name__ == "__main__":
    str1 = u"パトカー"
    str2 = u"タクシー"
    print(str1)
    print(str2)
    str3 = ""
    for i in range(len(str1)):
        str3 += str1[i] + str2[i]
    print(str3)
