# now here for optimal solution what we do is use two pointer similar to last question go over the elements and check which is smaller and then increment that pointer to reach a state where both the values could be possibly equal once the values we found are equal append the value and increment both the pointers.

#time complexity -> O(n1) | space complexity -> O(N1) at worst case for returning the answer otherwise it is O(1). 
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

intersection = []
j = 0
i = 0
while i < len(arr1) and j < len(arr2):
    if arr1[i] < arr2[j]:
        i += 1
    elif arr1[i] > arr2[j]:
        j += 1
    else:
        intersection.append(arr1[i])
        i += 1
        j += 1


print(*intersection)