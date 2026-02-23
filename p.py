from decimal import Decimal, getcontext
import sys

digits = int(input("кол-ов символов?\n"))
getcontext().prec = digits + 5

a = Decimal(1)
b = Decimal(1) / Decimal(2).sqrt()
t = Decimal(1) / Decimal(4)
p = Decimal(1)

iterations = 20

for i in range(1, iterations + 1):
    a_next = (a + b) / 2
    b = (a * b).sqrt()
    t -= p * (a - a_next)**2
    a = a_next
    p *= 2

    length = 20
    filled = int(length * i // iterations)
    bar = "#" * filled + "-" * (length - filled)

    sys.stdout.write(f"\rПрогресс: [{bar}] {i}/20")
    sys.stdout.flush()

pi = ((a + b)**2) / (4 * t)

sys.stdout.write("\r" + " " * 20 + "\r")
sys.stdout.flush()

pi_str = str(pi)[:digits + 2]
print(f"π = {pi_str}")
