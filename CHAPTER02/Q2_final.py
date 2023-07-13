import random

while True:
    s = random.choice([chr(ord("a") + i) for i in range(26)])
    print(s)
    if "r" in s or "t" in s:
        break
