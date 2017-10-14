# -*- coding: utf-8 -*-
# Typoglycemia
import random

def Typoglycemia(text):
    words = text.split()
    result = ""
    for word in words:
        wordList = list(word)
        if len(word) >= 4:
            tmp = wordList[1:-1]
            random.shuffle(tmp)
            result += wordList[0] + "".join(tmp) + wordList[-1]
        else:
            result += word
        result += " "
    print(result)

if __name__ == "__main__":
    text = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
    print(text)
    Typoglycemia(text)
