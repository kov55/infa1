import math
P = [int(x) for x in input("введите элементы массива: ").split()]

K = 0
S2 = 0

for p in P:
    if p > 0:
        K += 1
    S2 += p**2

print("исходный:", P)
print("пол. эл:", K)
print("квадрат суммы:", S2)
