#brute force solution for this question just make new array and append it into the new one amd make a set of it 
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

union = []
for i in arr1:
    union.append(i)

for i in arr2:
    union.append(i)
    
print(*list(set(union)))
# better appraoch 
# the brute force or possible solution is that we make a temporary array and then iterate over the given array and then append the smaller element but also check this time that does the elemen belong to the temporary element or not if does not belong in temporary array then append it if it does then no not append the value and just incremnet the pointer.


# the optimal solution for this will be go through both arrays using two pointers find if the number we are at is equal to the last element of out result array or not if its equal then just increment it cause we already has that in out array hence dont need it if its not same which number is lesser and append then lesser element and incremenet it at the end there will be posibility that either one of the arrays is not completely interated hence run two more loops with same condition to check and then append in the result array based on the condition.

# time complexity here is O(n1 + n2) | space complexity -> O(N) [worst case and that too is to return the result if we dont consider that then complexity is O(1)]
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

val = arr1[0] if arr1[0] < arr2[0] else arr2[0]
union = [val]
j = 0
i = 0
while i < len(arr1) and j < len(arr2):
    if arr1[i] == union[-1]:
        i += 1
    elif arr2[j] == union[-1] :
        j += 1
    elif arr1[i] < arr2[j]:
        union.append(arr1[i])
        i += 1
    elif arr1[i] > arr2[j]:
        union.append(arr2[j])
        j += 1

if j<len(arr2):
    while j < len(arr2):
        if arr2[j] != union[-1]:
            union.append(arr2[j])
        j += 1
if i<len(arr1):
    while j < len(arr1):
        if arr1[i] != union[-1]:
            union.append(arr1[i])
        i += 1

print(*union)