# -*- coding: utf-8 -*-
"""13.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/18WpdU2YEbK-MnisueubayjOo9ANd25KT
"""



#https://programmers.co.kr/learn/courses/30/lessons/76501

def solution(absolutes, signs):
    num = []
    for i in range(len(absolutes)):
        if signs[i] == True:
            num.append(absolutes[i])
        else:
            num.append(-absolutes[i])
    answer = sum(num)
    return answer