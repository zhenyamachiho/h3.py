import random

num = [random.randint(1, 100) for i in range(0, int(input()))]
print(num)

x = int(input())

num = [random.randint(1, 100) if i == x else i for i in num]
print(num)

c = 0
c1 = num[0]
for i in num:
    if c < i < x:
        c = i
    elif c1 > i > x:
        c1 = i

if c == 0:
    c = 'no'
if c1 < x:
    c1 = 'no'
print(c)
print(c1)
