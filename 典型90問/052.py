n = int(input())

a = []

for i in range(n):
    a_in = list(map(int, input().split(" ")))
    a.append(a_in)
    
MOD = 10 ** 9 + 7

sums = [sum(a[i]) for i in range(n)]

ans = 1

for i in range(n):
    ans *= sums[i]
    ans %= MOD
    
print(ans)