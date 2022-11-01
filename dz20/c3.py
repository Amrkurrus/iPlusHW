print("Enter the names of cities and their distance from Astana by 'space'.")
print("Enter 'stop' when you want to stop.")
i = ""
mdis = 0
mname = ''
while True:
    line = input()
    if line == "stop":
        break
    city, dis = line.split()
    if int(dis) > mdis:
        mdis = int(dis)
        mname = city
print(f"{mname}: {mdis}")