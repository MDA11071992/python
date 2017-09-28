N = int(input())
M = int(input())
x = int(input())
y = int(input())
if x > N or y > M:
    N, M = M, N
if x != 0 and y != 0:
    if x > N / 2:
        x = N - x
    if y > M / 2:
        y = M - y
print(y if x > y else x)
