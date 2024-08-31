# here to move the zeros to end of the array the brute force approach will be to run a loop and store all the non zero elements in a temporary array and then later on assign those values from the temp array to the original array and then rest of the array run another loop and fill it with zeros so to get the required answer the time complexity is O(2N)

# a slightly better approach or just a enhancement will be when we are appending the non zero values to the array at the same time we assign that index with a value of 0 so that we dont have to seperately run a loop and assign zeros at the end it will be already there hence the complexity will be O(2N - T) where t is the number of zeros.


# time -> O(2n - t) | space -> O(N)
nums = list(map(int, input().split()))
n = len(nums)

temp = []
for i in range(len(nums)):
    if nums[i] != 0:
        temp.append(nums[i])
        nums[i] = 0

for i in range(len(temp)):
    nums[i] = temp[i]

print(*nums)


# the optimal approach will be two pointer approach, first find the first zero from the array and then run another loop from the index of first zero found and then have another pointer first pointer will go and check is the number is non zero if it is swap it with the zero index keep doing it until end of the array 
# the time complexity in this case will be O(N) -> [first to find first zero + till end to swap with non zero] | space complexity here is O(1) as there is no temporary array here and we are only using varibles.
nums = list(map(int, input().split()))
n = len(nums)

j = -1
for i in range(n):
    if nums[i] == 0:
        j = i
        break

for i in range(j+1,n):
    if nums[i] != 0:
        nums[i],nums[j] = nums[j],nums[i]
        j+=1
    

print(*nums)