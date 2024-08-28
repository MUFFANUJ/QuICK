# in selection sort we were takin the minimum to the front but in bubble sort we push the maximum to the last by swapping adjacent values

#the worst and the average time complexity is O(n^2) where as adding a condition for checking everytime if the array is sorted or not will make the best time complexity O(N)

#one solution 
arr = list(map(int, input().split()))

for i in range(len(arr)-1):
  for j in range(len(arr)-i-1):
    if arr[j] > arr[j+1]:
      temp = arr[j+1]
      arr[j+1] = arr[j]
      arr[j] = temp
  
print(*arr)

#reverse solution with condition
arr = list(map(int, input().split()))
for i in range(len(arr)-1,0,-1):
  isSwapped = False
  for j in range(i):
    if arr[j] > arr[j+1]:
      temp = arr[j+1]
      arr[j+1] = arr[j]
      arr[j] = temp
      isSwapped = True
      
  if not(isSwapped):
    break

print(*arr)
  
