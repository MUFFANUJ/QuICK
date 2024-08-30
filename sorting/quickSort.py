# here we pick one pivort and place it in its correct position in the array and then dive the array in left and right part and repeat the same steps again take the pivort and place it in its correct position until we reach one element in our imaginary array one element is always sorted hence it sorts the array 

# the time complexity is as same as merge sort O(n*log n) but here we are not having any temporary array so the space complexity here is O(1) (excluding the recurrsion stack space) because we are only using the variables low and high.

# this follows the fundamental of divide and conqueror

arr = list(map(int, input().split()))

def arrange(arr,low,high):
  pivot = arr[low]
  i = low
  j = high
  while i < j:
    while arr[i] <= pivot and i <= high-1:
      i += 1
    while arr[j] > pivot and j >= low+1:
      j -= 1
      
    if i < j:
      arr[i] , arr[j] = arr[j], arr[i]
      
  arr[low],arr[j] = arr[j] , arr[low]
  return j
  
  
def action(arr,low,high):
  if low >= high :
    return 
  mid = arrange(arr,low,high)
  action(arr,low,mid-1)
  action(arr,mid+1,high)
  
  

action(arr,0,len(arr)-1)
print(*arr)
  
