import time
import os

prev_time = time.time()

try:
    t_input = input("durability = ").strip()
    t = float(t_input) if t_input else 0.1
except ValueError:
    t = 0.1

try:
    size_input = input("size (default 32) = ").strip()
    max_size = int(size_input) if size_input else 32
except ValueError:
    max_size = 32

for size in range(max_size + 1):
    now = time.time()
    delta = now - prev_time
    fps = 1 / delta if delta > 0 else 0
    prev_time = now

    os.system("clear")

    print(f"frame: {size}/{max_size}")
    print(f"fps: {fps:.2f}")
    print()

    for y in range(size):
        line = " " * (size - y - 1)
        for x in range(y + 1):
            if x & (y - x) == 0:
                line += "∆ "
            else:
                line += "  "
        print(line)

    time.sleep(t)
