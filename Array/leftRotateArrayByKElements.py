#To rotate an array first we need to think how we can rotate a single element 
# we can just go take the first element store it in some varible and then just shift other all elements by one lesser index and then place the value of the varible in the last index now if we have to do it for k elements we can run this loop for k time but this is brute force as it will have the time complexity of O(K*N) hence one thing to optimise this complexity is we can first store the first k elements in a temporary array and then shift other all elements from k+1 index or N-K index to the last to the first and so on and then just place the values stored in the temporary varibles inside the original array after tha n-k index

#brute force approach -> O(T*N)
t = int(input())
arr = list(map(int, input().split()))

for i in range(t%len(arr)):
  index = 0
  for i in range(1,len(arr)):
    arr[index],arr[i] = arr[i],arr[index]
  
    
print(*arr)

# better approach -> O(T+N) | space complexity = O(N) [worst case]
t = int(input())
arr = list(map(int, input().split()))

temp = arr[:t]

for i in range(t,len(arr)):
    arr[i-t] = arr[i]

for k in range(len(arr)-t,len(arr)):
    arr[k] = temp[k-(len(arr)-t)]
  
    
print(*arr)

# for the most optimal appraoch we have is we can reverse the elements till the k elements and also reverse the other half after k elements till the end and at last reverse the whole array that will also give the correct answer here


# time complexity -> O(2N) | space complexity is O(1) here the time complexity is slightly higher than the above case but here the space complexity is in constant time as we are not having any array.

k = int(input())
nums = list(map(int, input().split()))

n = len(nums)
k = k % n  
nums[:] = nums[::-1]

nums[:k] = nums[:k][::-1]

nums[k:] = nums[k:][::-1]

print(*nums)


# similarly find the solution for right rotating the array