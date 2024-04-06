n, k = map(int, input().split(" "))

MOD = 10 ** 9 + 7

if n == 1:
    print(k % MOD)
elif n == 2:
    print(k * (k - 1) % MOD)
else:
    print(k * (k - 1) * pow(k - 2, n - 2, MOD) % MOD)