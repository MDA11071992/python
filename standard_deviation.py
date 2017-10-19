import math

x = int(input())
n, sum, square_sum = 0, 0, 0
while x != 0:
    sum += x
    n += 1
    square_sum += x * x
    x = int(input())
else:
    sum /= n
    sigma = math.sqrt((square_sum - sum * sum * n) / (n - 1))
print(sigma)
