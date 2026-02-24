import sys
import math
from decimal import Decimal, getcontext

digits = int(input("Введите количество знаков Пи: "))
getcontext().prec = digits + 10

iterations = math.ceil(math.log2(digits)) if digits > 0 else 1

a = Decimal(1)
b = Decimal(1) / Decimal(2).sqrt()
t = Decimal(1) / Decimal(4)
p = Decimal(1)

for i in range(1, iterations + 1):
    a_next = (a + b) / 2
    b = (a * b).sqrt()
    t -= p * (a - a_next)**2
    a = a_next
    p *= 2
    
    fill = int(30 * i // iterations)
    bar = "#" * fill + "-" * (30 - fill)
    sys.stdout.write(f"\rВычисление: |{bar}| {i}/{iterations}")
    sys.stdout.flush()

pi_val = ((a + b)**2) / (4 * t)
pi_str = str(pi_val)[:digits + 2]

sys.stdout.write("\n\nРезультат:\n")
print(pi_str)
