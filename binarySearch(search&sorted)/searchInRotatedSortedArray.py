""" 
1. **Identify the sorted half**
   - Compute `mid` and check if `arr[mid] == target`. If true, return `mid`.
   - Check if the **left half is sorted** (`arr[low] <= arr[mid]`).
     - If `target` lies within this sorted half (`arr[low] <= target <= arr[mid]`), search in the left half (`high = mid - 1`).
     - Otherwise, search in the right half (`low = mid + 1`).
   - If the left half is not sorted, then the **right half must be sorted**.
     - If `target` lies within this sorted half (`arr[mid] <= target <= arr[high]`), search in the right half (`low = mid + 1`).
     - Otherwise, search in the left half (`high = mid - 1`).

2. **End Condition**
   - If `low > high`, `target` is not in the array, so return `-1`.
"""

def lowerSearch(arr, n , target):
    low = 0
    high = n-1
    while(low<=high):
        mid = (low+high)//2
        if arr[mid] == target:
            return mid
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

    
arr = list(map(int,input("Enter the array: ").split()))
target = int(input("Enter the target element: "))
print(lowerSearch(arr,len(arr),target))