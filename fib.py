fib = int(input())
a = 0
b = 1
x = int()
while a < fib:
    a, b = b, a + b
    x += 1
    if a == fib:
        print(x)
    elif a > fib:
        print("Don't FIB")