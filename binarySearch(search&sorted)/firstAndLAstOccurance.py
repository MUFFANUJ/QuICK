#first and last occurance of a element through linear iteration - O(N)
def binarySearch(arr, n , target):
    first , last = -1,-1
    for i in range(n):
        if arr[i] == target:
            if first == -1:
                first = i
            last = i
    return [first,last]    

arr = list(map(int,input("Enter the array: ").split()))
target = int(input("Enter the target element: "))
print(binarySearch(arr,len(arr),target))


#everytime when we want to perform search in a sorted space think of binary search
# here we can use lower bound and upper bound logic as it will give the least and most occurance 
# ex - arr = [3,4,5,6,7,8,8,8,8,10,11] so lower_bound will give 5 and upper_bound will give 9 hence [lower_bound , upper_bound -1]
# will be the answer but there are some edge cases with lower bound calculation if element is not present for example 9 is not
# present in the array then in that case it will give 9 as index of value 10  which is not equal to 9 also if we have a value
# greater than the max element of array for example 12 then the lower_bound will give hypothetical index as 11 which is equal to
# the length of the array hence we have to take care of these cases 
# TC - 2 * O(log N) SC - O(1)
def binarySearch(arr, n , target):
    lb = lower_bound(arr,n,target)  #assuming there is a function which calculates lower_bound 
    if arr[lb] != target or lb == n:
        return [-1,-1]

    return [ lower_bound, upper_bound -1]


arr2 = list(map(int,input("Enter the array: ").split()))
target = int(input("Enter the target element: "))
print(binarySearch(arr,len(arr2),target))


# using pure binary search and none of lower bound or upper bound concept 
def lowerSearch(arr, n , target):
    low = 0
    high = n-1
    first = -1
    while(low<=high):
        mid = (low+high)//2
        if arr[mid] == target:
            first = mid
            high = mid -1
        elif arr[mid] < target:
            low = mid+1
        else:
            high = mid -1
    return first

def upperSearch(arr, n , target):
    low = 0
    high = n-1
    last = -1
    while(low<=high):
        mid = (low+high)//2
        if arr[mid] == target:
            last = mid
            low = mid+1
        elif arr[mid] < target:
            low = mid+1
        else:
            high = mid -1
    return last
    
arr = list(map(int,input("Enter the array: ").split()))
target = int(input("Enter the target element: "))
print(lowerSearch(arr,len(arr),target),upperSearch(arr,len(arr),target))  #can add a check here to find if first == -1 if so then 
                                                                        # directly return [-1,-1] it might save a lot of computation if element is not there.