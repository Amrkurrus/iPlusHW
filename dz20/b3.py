print("Enter the number of teams")
teamN = int(input())
print("Enter number of team and their schores by 'space'")
n0 = 100
score0 = 0
for i in range(teamN):
    n1, score1 = map(int, (input().split()))
    if (n0 < n1 and score0 < score1) or (n0 > n1 and score0 > score1):
        print("Команды перечислены не в соответствии с их местами!")
        break
    n0 = n1
    score0 = score1
else:
    print("Команды перечислены в соответствии с их местами.")
