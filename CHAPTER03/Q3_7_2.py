<<<<<<< HEAD
with open("numbers.txt", "r") as f:
=======
with open("number.txt", "r") as f:
>>>>>>> 35f1cabc672e34120893bfa1be0d1919dce7204d
    sum = 0
    for data in f:
        num = int(data)
        sum += num
    print(sum)
