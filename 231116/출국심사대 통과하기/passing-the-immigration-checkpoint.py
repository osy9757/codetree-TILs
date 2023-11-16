N = int(input())
checkTime = [list(map(int,input().split())) for _ in range(N)]
checkTime.sort()
for i in range(0,N-1):
    checkTime[i][1] += checkTime[i][0]
    if checkTime[i+1][0] <= checkTime[i][1]:
        checkTime[i+1][0] = checkTime[i][1]
print(checkTime[-1][1]+ checkTime[-1][0])