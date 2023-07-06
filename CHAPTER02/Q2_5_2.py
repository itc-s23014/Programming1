answer = "\n".join(
    [" ".join(["w" if i == j else "b" for j in range(4)]) for i in range(4)]
)
print(answer)
