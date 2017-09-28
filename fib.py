fib = int(input("enter number: "))
a = 0
b = 1
x = 1
for i in range(fib * 1000):
    a, b = b, a + b
    x += 1
    if fib == a:
        print(x)
        break
else:
    print("Don't FIB")