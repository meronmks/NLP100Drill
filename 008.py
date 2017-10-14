# -*- coding: utf-8 -*-
# 暗号文

def cipher(text):
    result = ""
    for i in range(len(text)):
        if ord(text[i]) >=97 and ord(text[i]) <= 122:
           result += chr(219 - ord(text[i]))
        else:
            result += text[i]
    return result

if __name__ == "__main__":
    text = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
    print(text)
    text = cipher(text)
    print(text)
    print(cipher(text))
