arr = list(map(int, input().split()))
for i in range(len(arr)-1):
  minIndex = i
  for j in range(i,len(arr)):
    if arr[j] < arr[minIndex]:
      minIndex = j
  temp = arr[minIndex]
  arr[minIndex] = arr[i]
  arr[i] = temp
  
print(*arr)

# in selection sort what we do is we take one element from start and find the minimum from the rest of the array and then interchange the values interchange with minimum value with the current value 

# time complexity here is (n*(n+1))/2 which is nothing but O(n^2) it is the (best, average and worst)
