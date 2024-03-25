import math

a, b, c = map(int, input().split(" "))
gcd_abc = math.gcd(a, b, c)
a_num = a // gcd_abc
b_num = b // gcd_abc
c_num = c // gcd_abc

result = a_num + b_num + c_num - 3

print(result)