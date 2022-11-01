asum = 0
for i in range(2, 11):
    asum += i / (i + 1)
print(asum)

bsum = 0
low_num = 1
for _ in range(0, 9):
    bsum = bsum + 1 / low_num
    low_num *= 3
print(bsum)