n = 13#int(input("Enter the number: "))
m = 2 * n + 3
for i in range(m):
    for j in range(m):
        if j == 0 or j == m - 1:
            print("O ", end="")
        elif i == 0 or i == m - 1:
            print("0 ", end="")
        elif i == n + 1 and j == n + 1:
            print("O ", end="")
        elif i < n + 1 and j < n + 1 and i < j + 1:
            num = n - j + 1
            print(f"{num:<2}", end="")
        elif i < n + 1 and j > n + 1 and i + j > m - 2:
            num = m - 1 - j
            print(f"{num:<2}", end="")
        elif i > n + 1 and j < n + 1 and i + j < m:
            num = j
            print(f"{num:<2}", end="")
        elif i > n + 1 and j > n + 1 and i + 1 > j:
            num = j - n - 1
            print(f"{num:<2}", end="")
        else:
            print("  ", end="")
    print()