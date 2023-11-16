N = int(input())
checkTime = sorted([list(map(int, input().split())) for _ in range(N)])
for i in range(N - 1):
    checkTime[i][1] += checkTime[i][0]
    checkTime[i + 1][0] = max(checkTime[i + 1][0], checkTime[i][1])
print(sum(checkTime[-1]))