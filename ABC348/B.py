n = int(input())
x = []
y = []
for i in range(n):
    a, b = map(int, input().split(" "))
    x.append(a)
    y.append(b)

dists = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        dists[i][j] = (x[i] - x[j]) ** 2 + (y[i] - y[j]) ** 2
    max_dist_index = dists[i].index(max(dists[i]))
    print(max_dist_index + 1)
