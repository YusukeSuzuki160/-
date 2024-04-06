n = int(input())
a = list(map(int, input().split(" ")))
b = list(map(int, input().split(" ")))
c = list(map(int, input().split(" ")))

number_list_a = [0] * 46
number_list_b = [0] * 46
number_list_c = [0] * 46

for i in range(n):
    number_list_a[a[i] % 46] += 1
    number_list_b[b[i] % 46] += 1
    number_list_c[c[i] % 46] += 1

result = 0
for i in range(46):
    for j in range(46):
        for k in range(46):
            if (i + j + k) % 46 == 0:
                result += number_list_a[i] * number_list_b[j] * number_list_c[k]
                
print(result)