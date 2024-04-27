n = int(input())

a = []
b = []

for i in range(n):
    a_ = input()
    a.append(a_)

for i in range(n):
    b_ = input()
    b.append(b_)

for i in range(n):
    for j in range(n):
        if a[i][j] != b[i][j]:
            print(f"{i+1} {j+1}")

