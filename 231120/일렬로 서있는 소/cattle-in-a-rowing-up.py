N = int(input())
dots = [int(input()) for _ in range(N)]
countNum=0
dots.sort()

for i in range(N-2):
    for j in range(i+1,N-1):
        for k in range(j+1,N):
            if dots[j] - dots[i] <= dots[k] - dots[j] <= 2*(dots[j] - dots[i]):
                countNum+=1

print(countNum)