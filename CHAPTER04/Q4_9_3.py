N = int(input())
a = []

for _ in range(N):
    num = int(input())
    a.append(num)

for i in range(N):
    for j in range(i + 1, N):
        if a[i] < a[j]:
            a[i], a[j] = a[j], a[i]

print(" ".join(map(str, a)))
