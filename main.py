## importing bibliotecs 

import numpy as np

## desvio padrão

def DesvioP(N, M, i):
    S = 1/N-1*(M-i)**2
    return S

## data

vl = np.genfromtxt('')#, dtype= None, delimiter= None)

N = float(input())
M = float(input()) # calcular media baseada nos valores
i = np.zeros(int(N))

for k in range(int(N)):
     i[k] = vl[0+k]

print(N, M, i)

for l in range(int(N)):
     Dp = DesvioP(N, M, i[l])
     
print(Dp)
