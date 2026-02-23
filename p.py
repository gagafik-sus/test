from decimal import Decimal, getcontext
import os

digits = int(input("Сколько знаков после запятой? "))
getcontext().prec = digits + 10

a = Decimal(1)
b = Decimal(1) / Decimal(2).sqrt()
t = Decimal(1) / Decimal(4)
p = Decimal(1)

for _ in range(25):
    a_next = (a + b) / 2
    b = (a * b).sqrt()
    t -= p * (a - a_next)**2
    a = a_next
    p *= 2

pi = ((a + b)**2) / (4 * t)
pi_str = str(pi)[:digits + 2]

print(f"\nPi = {pi_st
                r}")
