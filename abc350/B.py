n, q = map(int, input().split())
t = list(map(int, input().split()))

teeth = [True] * (n)

for _t in t:
    teeth[_t - 1] = not teeth[_t - 1]

print(teeth.count(True))