# -*- coding: utf-8 -*-
# 円周率

if __name__ == "__main__":
    str1 = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
    str1 = str1.replace(",", "")
    str1 = str1.replace(".", "")
    str1 = str1.split()
    list = []
    for word in str1:
        list.append(len(word))
    print(list)
