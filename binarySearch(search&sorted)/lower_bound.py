def binarySearch(arr, n , target):
    low = 0
    high = n-1
    ans = n
    while(low<=high):
        mid = (low+high)//2
        if arr[mid] >= target:
            ans = mid
            high = mid -1
        else:
            low = mid+1
    return ans

arr = list(map(int,input("Enter the array: ").split()))
target = int(input("Enter the target element: "))
print(binarySearch(arr,len(arr),target))

#this single arrpoach solves a lot of problems like searching and inserting a value in an array 
# ceil value in ana array
 