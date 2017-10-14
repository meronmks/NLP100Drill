# -*- coding: utf-8 -*-
# 元素記号

if __name__ == "__main__":
    str1 = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
    str1 = str1.replace(",", "")
    str1 = str1.replace(".", "")
    str1 = str1.split()
    gram = [1, 5, 6, 7, 8, 9, 15, 16, 19]
    dic = {}
    for i in range(len(str1)):
        if i + 1 in gram:
            dic[i] = str1[i][:1:1]
        else:
            dic[i] = str1[i][:2:1]
    print(dic)
