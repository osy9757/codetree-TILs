N = int(input())
names = [list(map(str, input().split())) for _ in range(N)]

for name in names:
    name.sort()
names.sort()
count=1
maxCount=0
for i in range(N-1):
    if names[i] == names[i+1]:
        count+=1
    else:
        maxCount=max(count,maxCount)
        count=1
        
maxCount=max(count,maxCount)     
print(maxCount)