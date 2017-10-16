n = 1
x = int()
y = int()
s = 1
i = int()
while n != 0:
    n = int(input())
    x, y = y, n
    i = s if i < s else i
    s = 1 if x != y else s + 1
print(i)
