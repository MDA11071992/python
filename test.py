n = int(input())
a = 0
b = 1
while n != 0:
    if n > a:
        a, c = n, a
    if a == c == n:
        b += 1
    n = int(input())
print(b)    