n = int(input())

index_list = [0] * n
a = list(map(int, input().split()))

for i in range(n):
    a_in = a[i]
    index_list[a_in - 1] = i
    
count = 0
swap_result = []

for i in range(n):
    if a[i] != i + 1:
        count += 1
        _a = a[i] - 1
        a[i] = i + 1
        a[index_list[i]] = _a + 1
        a_index = index_list[i]
        index_list[_a] = index_list[i]
        index_list[i] = i
        swap_result.append((i + 1, a_index + 1))

print(count)
for swap in swap_result:
    print(*swap)