b23 = ''
a = 23
whule a != 0:
    a, r = divmod(a, 2)
    b23 = str(r) + b23
print(b23)
a, r1 = divmod(23, 2)
a, r2 = divmod(a, 2)
a, r3 = divmod(a, 2)
a, r4 = divmod(a, 2)
a, r5 = divmod(a, 2)
a
print(r5, r4, r3, r2, r1)
