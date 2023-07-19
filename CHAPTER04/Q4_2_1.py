def number_to_day(num=0):
    if num == 0:
        day = "Wednesday"
    elif num == 1:
        day = "Thursday"
    elif num == -1:
        day = "Tuesday"
    else:
        day = "Invalid input"
    return day


s = input("入力")
result = number_to_day(s)
print(result)
