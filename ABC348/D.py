h, w = map(int, input().split(" "))
a = [input() for _ in range(h)]
n = int(input())
rc = []
e = []
for i in range(n):
    r_, c_, e_ = map(int, input().split(" "))
    rc.append((r_ - 1, c_ - 1))
    e.append(e_)
for i in range(n):
    for j in range(h):
        if a[i][j] == "S":
            start_index = (i, j, 0)

queue = [start_index]

while queue:
    i, j, energy = queue.pop(0)
    if (i, j) in rc and energy < e[rc.index((i, j))]:
        energy = e[rc.index((i, j))]
    if energy == 0 and a[i][j] != "T":
        continue
    if a[i][j] == "T":
        print("Yes")
        exit()
    if i + 1 < h and a[i + 1][j] != "#":
        queue.append((i + 1, j, energy - 1))
    if j + 1 < w and a[i][j + 1] != "#":
        queue.append((i, j + 1, energy - 1))
    if i - 1 >= 0 and a[i - 1][j] != "#":
        queue.append((i - 1, j, energy - 1))
    if j - 1 >= 0 and a[i][j - 1] != "#":
        queue.append((i, j - 1, energy - 1))


print("No")