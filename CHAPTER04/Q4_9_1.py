def bubble_sort_descending(data):
    n = len(data)
    for i in range(n - 1):
        
        for j in range(n - i - 1):
            if data[j] < data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]

    return data

if __name__ == "__main__":
    N = int(input())
    data = []
    for _ in range(N):
        d = int(input())
        data.append(d)

    sorted_data = bubble_sort_descending(data)
    print(*sorted_data)
