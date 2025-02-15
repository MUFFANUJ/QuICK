#here we are finding out the sorted part then storing the minimum in an varible later find the sorted part again and comapring 
#for the minimum and at last we have the smallest element once the algorithm runs out of options 

# now we can have one more otimization in this is we can add a check for checking if we have the whole array sorted 
# for ex - arr[low] < arr[high] will tell us if whole array is sorted or not if we find the whole array is sorted
# there is no need to perfofm further binary search we can directly compare and return the minimum 


#TC - O(log n) base 2 SC - O(1)
def lowerSearch(arr, n ):
    low = 0
    high = n-1
    ans = float('inf')
    while(low<=high):
        mid = (low+high)//2
        if arr[low] <= arr[high]:
            ans = min(ans,arr[low])
            break
        if arr[low] <= arr[mid]:
            ans = min(ans,arr[low])
            low = mid + 1
        else:
            ans = min(ans,arr[mid])
            high = mid - 1
            
    return ans

    
arr = list(map(int,input("Enter the array: ").split()))
print(lowerSearch(arr,len(arr)))