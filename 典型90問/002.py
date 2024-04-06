from itertools import combinations
n = int(input())

if n % 2 == 1:
    print()
else:
    numbers = [i for i in range(n)]
    combs = list(combinations(numbers, n // 2))
    for comb in combs:
        check = 0
        for i in range(n):
            if i not in comb:
                check -= 1
            else:
                check += 1
            if check < 0:
                break
        if check == 0:
            for i in range(n):
                if i in comb:
                    print('(', end='')
                else:
                    print(')', end='')
            print()