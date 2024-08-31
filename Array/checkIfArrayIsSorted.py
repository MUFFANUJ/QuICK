arr = list(map(int,input().split()))

msg = "NO"
for i in range(len(arr)-1):
    if(arr[i] > arr[i+1]):
        msg = "NO"
        break
    else:
        msg = "YES"
print(msg)
