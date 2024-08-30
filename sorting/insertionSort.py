# here we take an element one by one in our array and place that element in its correct position or order ,start with two elements and keep going till last element 

#oneway
arr = list(map(int, input().split()))
for i in range(len(arr)):
  for j in range(i,0,-1):
    if arr[j] < arr[j-1]:
      temp = arr[j-1]
      arr[j-1] = arr[j]
      arr[j] = temp
      

print(*arr)
  
# the worst case and average case time complexity is again O(n^2) and with using a while loop instead of for loop 
arr = list(map(int, input().split()))
for i in range(len(arr)):
  j = i
  while j>0 and arr[j] < arr[j-1]:
      temp = arr[j-1]
      arr[j-1] = arr[j]
      arr[j] = temp
      j-=1

print(*arr)
  
# now if we encounter an already sorted array we get a time complexity of O(N) which is its best case.