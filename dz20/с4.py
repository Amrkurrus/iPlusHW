number = int(input())
i = 2
while i < number:
    if number % i == 0:
        print("Число не простое.")
        break
    i += 1
else:
    print("Число простое!")