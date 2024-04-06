def cut(a, m):
    count = 0
    pre = 0
    for i in a:
        if i - pre >= m and l - i >= m:
            count += 1
            pre = i
    return count

n, l = map(int, input().split(" "))
k = int(input())
a = list(map(int, input().split(" ")))

start = -1
end = l + 1

while end - start > 1:
    mid = (start + end) // 2
    if cut(a, mid) < k:
        end = mid
    else:
        start = mid

print(start)