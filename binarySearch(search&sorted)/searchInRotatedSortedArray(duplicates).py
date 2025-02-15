#the approach used in the previous problem wont work here because there can be some edge cases where the 
#start mid and end postion value are the same for example - arr = [3,1,2,3,3,3,3] so here we cant compare 
#or find which part is sorted programmatically (also we cant find the index or target element in this case using binary 
#search we have to use linear search only) -> question made using this would be to find if the element exist in this or not


# the solution for this problem is to trim down the search space everytime we find arr[low] = arr[mid] = arr[high]
# hence trimming the search space will at some point bring me to the point where i might be able to compare and find the sorted area.

# just adding this condition 
# if arr[low] == arr[mid] and arr[mid] == arr[high]:
#     low += 1
#     high -= 1
#     continue        # continue because there might be more duplicates like arr = [3,3,2,3,3,3,3] in this case it needs to again trim it down

def lowerSearch(arr, n , target):
    low = 0
    high = n-1
    while(low<=high):
        mid = (low+high)//2
        if arr[mid] == target:
            return mid
        
        if arr[low] == arr[mid] and arr[mid] == arr[high]:
            low += 1
            high -= 1
            continue  

        if arr[low] <= arr[mid]:
            if arr[low] <= target and target <= arr[mid]:
                high = mid -1
            else:
                low = mid +1
        else:
            if arr[mid] <= target and target <= arr[high]:
                low = mid + 1
            else:
                high = mid - 1
    return -1

#TC - average = O(log n) worst = O(N/2)
    
arr = list(map(int,input("Enter the array: ").split()))
target = int(input("Enter the target element: "))
print(lowerSearch(arr,len(arr),target))