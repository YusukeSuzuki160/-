from collections import Counter

s = input()

counter = Counter(s)

for i in range(1, (len(s)+1)):
    i_appear_alfa = {key: value for key, value in counter.items() if value == i}
    if len(i_appear_alfa) != 0 and len(i_appear_alfa) != 2:
        print("No")
        exit()

print("Yes")