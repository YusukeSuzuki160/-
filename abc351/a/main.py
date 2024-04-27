a = list(map(int, input().split(" "))) 
b = list(map(int, input().split(" ")))

takahasi_point = sum(a)
aoki_point = sum(b)

print(takahasi_point - aoki_point + 1)