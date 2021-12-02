# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 09:44:24 2021

@author: gjones
"""

import numpy as np

textinput = np.dtype([('dir', 'U1'), ('size', 'i')])
input = np.loadtxt('input.txt',dtype=textinput,usecols=(0,1))
V = H = 0

for i,change in enumerate(input):
    V = V - change['size'] if change['dir'] == 'u' else V
    V = V + change['size'] if change['dir'] == 'd' else V
    H = H + change['size'] if change['dir'] == 'f' else H

print('The final depth x distance is ' + str(H*V))

V1 = H1 = aim = 0
for i,change in enumerate(input):
    aim = aim - change['size'] if change['dir'] == 'u' else aim
    aim = aim + change['size'] if change['dir'] == 'd' else aim
    if change['dir'] == 'f':
        H1 = H1 + change['size'] 
        V1 = V1 + (aim * change['size']) 
print('The new final depth x distance is ' + str(H1*V1))