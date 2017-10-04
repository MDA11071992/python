x = int(input())
p1 = 5
p2 = 15
l = 45
u = 540
y = 1

while y <= x:
    u += l
    if y != x:
        if y % 2 == 0:
            u += p2
        else:
            u += p1
    y += 1

hour = u % 1440 // 60
minutes = u % 60
print(hour, minutes)
