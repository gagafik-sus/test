from decimal import Decimal, getcontext

digits = int(input("сколько чисел после запятой?\n"))

getcontext().prec = digits + 5

a = Decimal(1)
b = Decimal(1) / Decimal(2).sqrt()
t = Decimal(1) / Decimal(4)
p = Decimal(1)

for _ in range(20):
    a_next = (a + b) / Decimal(2)
    b = (a * b).sqrt()
    t -= p * (a - a_next)**2
    a = a_next
    p *= 2

pi = ((a + b)**2) / (4 * t)

pi_str = str(pi)[:digits + 2]
print(f"p = {pi_str}")
