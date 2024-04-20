n = int(input())
a = []
c = []
for i in range(n):
    a_, c_ = map(int, input().split(" "))
    a.append(a_)
    c.append(c_)
    

scores = {}

for a_, c_ in zip(a, c):
    if c_ in scores:
        scores[c_] = min(scores[c_], a_)
    else:
        scores[c_] = a_

print(max(scores.values()))