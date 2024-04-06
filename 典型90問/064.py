n, q = map(int, input().split(" "))
a = list(map(int, input().split(" ")))
l = []
r = []
v = []

for i in range(q):
    l_, r_, v_ = map(int, input().split(" "))
    l.append(l_)
    r.append(r_)
    v.append(v_)

inconvenience_list = [a[i] - a[i + 1] for i in range(n - 1)]
inconvenience = sum([abs(i) for i in inconvenience_list])
a_len = len(a)
for l_, r_, v_ in zip(l, r, v):
    if l_ > 1:
        left_before = abs(inconvenience_list[l_ - 2])
        inconvenience_list[l_ - 2] -= v_
        left = abs(inconvenience_list[l_ - 2])
        inconvenience += left - left_before
    if r_ < a_len:
        right_before = abs(inconvenience_list[r_ - 1])
        inconvenience_list[r_ - 1] += v_
        right = abs(inconvenience_list[r_ - 1])
        inconvenience += right - right_before
    print(inconvenience)