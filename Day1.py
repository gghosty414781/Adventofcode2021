# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 13:30:02 2021

@author: gjones
"""
import numpy as np

input = np.genfromtxt(fname='input.txt')
inputlength = len(input)
count = 0

for i in range(inputlength-3):
    input1 = input[i] + input[i+1] + input[i+2]
    input2 = input[i+1] + input[i+2] + input[i+3]
    if input2 > input1:
        count += 1
print(count)