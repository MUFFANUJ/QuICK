arr = list(map(int,input().split()))
hs = [0]*(max(arr)+1)
minFre = float('inf')
maxFre = float('-inf')
minEle = 0
maxEle = 0
for i in arr:
    hs[i] += 1
    
for i in hs:
    if i == 0: continue
    if minFre > i:
        minFre = hs[i]
        minEle = i
    if maxFre <= i:
        maxFre = hs[i]
        maxEle = i
    

print(maxEle,minEle)
