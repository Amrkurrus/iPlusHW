print("Enter the temperature in degrees celsius.")
print("Etner 'stop' when you stop.")
i = ""
counter = 0
while i != "stop":
    i = input()
    if i.isalpha():
        continue
    elif int(i) < 0:
        counter += 1
print(counter)
