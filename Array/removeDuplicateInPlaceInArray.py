# brute force approach is make a set and assign its value to the values of the array so it has first elements as sorted and give the length of the set but this takes O(n*log n) and space complexity is O(N).

# THE optimal solution include two pointer approach where we replace the one pointer with other once value when we find a different value than the current pointer

arr = list(map(int, input().split()))

i = 0
for j in range(len(arr)):
  if arr[j] != arr[i]:
    arr[i+1] = arr[j]
    i+=1
    
print(*arr)