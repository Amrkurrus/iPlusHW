from math import e


print("Banana cost")
banana_cost = 100
for d in range(2, 31):
    print(f"{d}: {d*banana_cost} tg")


print("\nHorizon distance")
R = 6350
def hordes( h, r=R): #Формула S = [(R+h)^2 - R^2]^1/2
    s = ((r + h) ** 2 - r ** 2) ** 0.5
    return s
for i in range(1, 10+1):
    print(f"{i}: {hordes(i):.2f} km")


print("\nAir density")
Po = 1.29
Z = 1.25 * 10 ** -4
def airden(h, po=Po, z=Z, e=e):
    p = po * e ** (h * z)
    return p
for i in range(0, 300+1, 30):
    if i == 0:
        print(f"{i+1}: {airden(i):.3f}")
    else:
        print(f"{i}: {airden(i):.3f}")


print("Engine power")
for i in range(1, 20+1):
    e = int(input())
    if e > 200:
        print(f"{i}: {e} hp")


print("Informatics")
for i in range(1,25+1):
    m = int(input())
    if m <= 2:
        print(f"{i}: {m} - Неудовлетворительно!")
