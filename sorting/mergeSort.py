# in merge sort we divide the given unsorted array into two and keep on dividing it until the array has one element and then we start to merge the array in a fastion that the resultant array is sorted likewise we divide and merge whole left side of the array first then whole right side and at last merge them both with some condition -> creating a temporaroy array is essential to store the answer later on which we use this temp array to assign the value on the correct place on the original array

arr = list(map(int, input().split()))

def merge(arr,low,mid,high):
  temp = []
  left = low
  right = mid + 1
  while left <= mid and right <= high:
    if arr[left] <= arr[right]:
      temp.append(arr[left])
      left += 1
    else:
      temp.append(arr[right])
      right += 1

  while left <= mid:
    temp.append(arr[left])
    left += 1
    
  while right <= high:
    temp.append(arr[right])
    right += 1
    
  for i in range(low,high+1):
    arr[i] = temp[i-low]

def action(arr,low,high):
  if low >= high :
    return 
  mid = (low + high)//2
  action(arr,low,mid)
  action(arr,mid+1,high)
  merge(arr,low,mid,high)
  
  

action(arr,0,len(arr)-1)
print(*arr)
  
# according to time complexity merge sort is better than bubble, insertion and selection it has a time complexity of O(n*log n) and space complexity of O(N).