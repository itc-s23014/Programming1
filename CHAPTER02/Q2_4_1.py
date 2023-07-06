b23 = ''
a = 23
whule a != 0:
    a, r = divmod(a, 2)
    b23 = str(r) + b23
print(b23)
