# the bruteForce solution is that we can sort the array and then until we find the second largest element i mean any number which is not equal to the largest number we stop and return that ex -> [1,7,7,7,7] so we need to sort and run a loop the time complexity in this case is O(n*log n + n)
# the better case is once time we find the maximum of the array and then again run a loop and find the second largest hence the time complexity is O(2N)

# the optimal case is when we just run one loop and perform both operation at same time 

arr = list(map(int, input().split()))

largest = arr[0] 
second = float('-inf')
for i in range(1,len(arr)):
  if largest < arr[i] :
    largest = arr[i]
  if second < arr[i] and largest > arr[i]:
    second = arr[i]
  
    
print(second)