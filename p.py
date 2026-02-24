from decimal import Decimal, getcontext
import sys
import math

digits = int(input("Сколько знаков Пи вычислить?\n"))
getcontext().prec = digits + 10 

iterations = math.ceil(math.log2(digits)) + 1

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

    fill = int(20 * i // iterations)
    sys.stdout.write(f"\rПрогресс: [{'#'*fill}{'-'*(20-fill)}] {i}/{iterations}")
    sys.stdout.flush()

pi = ((a + b)**2) / (4 * t)
pi_str = str(pi)[:digits + 2]

sys.stdout.write("\n")
print(p
      i_str)
