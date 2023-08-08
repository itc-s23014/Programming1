def x(*args, y="/"):
    return y.join(args)


retult = x("rukiya", "takaesu", "nahasi", "oroku")
print(retult)
