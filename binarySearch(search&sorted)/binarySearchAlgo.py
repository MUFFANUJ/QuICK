def binarySearch(arr, n , target):
    low = 0
    high = n-1
    while(low<=high):
        mid = (low+high)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid+1
        else:
            high = mid -1
    return -1

arr = list(map(int,input("Enter the array: ").split()))
target = int(input("Enter the target element: "))
print(binarySearch(arr,len(arr),target))


#time complexity : O(log n) base 2
#space complexity : 


#overflow case : low = int_max , high = int_max cant store 2*int_max in one variable  then mid = low + (high - low)/2 or take long long for c++