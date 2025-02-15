def binarySearch(arr, n , target):
    low = 0
    high = n-1
    ans = -1
    while(low<=high):
        mid = (low+high)//2
        if arr[mid] <= target:
            ans = mid               # why no need of checking if ans < mid cause binary search by default eliminates the 
            low = mid+1             #larger part and always shortens the array.
        else:
            high = mid -1
    return ans

arr = list(map(int,input("Enter the array: ").split()))
target = int(input("Enter the target element: "))
print(binarySearch(arr,len(arr),target))

#c++ stl has this directly lower_bound(arr,arr+n,n) [ - arr.begin()  arr.begin(), arr.end()] for vector 