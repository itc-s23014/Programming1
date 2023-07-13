import random

numbers = random.sample([str(i) for i in range(1, 10)], k=4)
num4 = "".join(numbers)

while True:
    val = input()
    if val == num4:
        print("OK")
        break
    else:
        print(val, ": NG")
