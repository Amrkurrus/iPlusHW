print("Enter the count of, em... I don't now. :")
S = 1000  # m
n = int(input())


def arman_idiot(n, s=S):
    total = 0
    for i in range(1, n+1):
        if i % 2 != 0:
            total += S / i
        else:
            total -= S / i
    return total

print(f"For the {n} attempts total distance from home is {arman_idiot(n):.2f} meters.")
print(f"For 50 attempts the outcome will be {arman_idiot(50):.2f} meters.")