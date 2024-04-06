n, k = map(int, input().split(" "))
a = []
b = []
for i in range(n):
    a_in, b_in = map(int, input().split(" "))
    a.append(a_in)
    b.append(b_in)
    
points = [0] * (2 * n)

for i in range(n):
    points[i] = b[i]
    points[i + n] = a[i] - b[i]

points.sort(reverse=True)

print(sum(points[:k]))