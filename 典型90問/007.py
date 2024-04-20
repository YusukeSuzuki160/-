import bisect

n = int(input())
a = list(map(int, input().split()))
q = int(input())
b = [int(input()) for _ in range(q)]

a = sorted(a)

for _b in b:
    idx = bisect.bisect_left(a, _b)
    if idx == 0:
        print(abs(a[idx] - _b))
    elif idx == n:
        print(abs(a[idx - 1] - _b))
    else:
        print(min(abs(a[idx] - _b), abs(a[idx - 1] - _b)))