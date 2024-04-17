import math
l, r = map(int, input().split(" "))

count = 0
print_str = []

if l == 0:
    right_index = math.floor(math.log2(r))
    
    right = 2 ** right_index
    count += 1
    print_str.append(f"0 {right}")

else:

    left_index = math.ceil(math.log2(l))
    right_index = math.floor(math.log2(r))

    left = 2 ** left_index
    right = 2 ** right_index

    left2 = left - l

    current = l
    
    add_num_stack = []

    while left2 > 0:
        add_num = 2 ** math.floor(math.log2(left2))
        add_num_stack.append(add_num)
        left2 = left2 - add_num
        count += 1
    
    while add_num_stack:
        add_num = add_num_stack.pop()
        print_str.append(f"{current} {current + add_num}")
        current += add_num
        
    for i in range(left_index, right_index):
        print_str.append(f"{2 ** i} {2 ** (i + 1)}")
        count += 1

current = right



right2 = r - right
while right2 > 0:
    add_num = 2 ** math.floor(math.log2(right2))
    right2 = right2 - add_num
    print_str.append(f"{current} {current + add_num}")
    current += add_num
    count += 1

print(count)
for s in print_str:
    print(s)