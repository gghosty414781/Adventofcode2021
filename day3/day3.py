from collections import Counter

gamma,eps = [],[]
with open('input.txt', 'rt') as f:
    input = [list(l) for l in f.read().splitlines()]
for c in range(len(input[0])):
    col = [input[i][c] for i in range(len(input))]
    most_common = Counter(col).most_common(1)[0][0]
    gamma.append(most_common)
    eps.append(str('1' if most_common == '0' else '0'))    
gamma,eps = int(''.join(gamma), 2), int(''.join(eps), 2)

print(gamma, eps, gamma * eps)

inputO=inputC=input
for c in range(len(inputO)):
    if len(inputO) == 1:
        break
    col = [inputO[i][c] for i in range(len(inputO))]
    ctr = Counter(col).most_common(2)
    most_common = ctr[0][0]
    if ctr[0][1] == ctr[1][1]:
        most_common = '1'
    inputO = [v for v in inputO if v[c] == most_common]
ox = int(''.join(inputO[0]), 2)
for c in range(len(inputC)):
    if len(inputC) == 1:
        break
    col = [inputC[i][c] for i in range(len(inputC))]
    ctr = Counter(col).most_common(2)
    most_common = ctr[0][0]
    if ctr[0][1] == ctr[1][1]:
        most_common = '1'
    inputC = [v for v in inputC if v[c] != most_common]
co2 = int(''.join(inputC[0]), 2)
print(ox, co2, ox * co2)