# the brute force appraoch is we run nested loops one from 1 to N and other one in the nums given array now check if the ith value is anywhere present in the array or not and if we dont find it we return the index ith value just keep a flag and change the flag value once the element if found if element is not found then break loops and return the answer. Here the time complexity will be O(n^2).

# the better approach is hashing we hash the values from 1 to N in a temporary array with initial values as 0 and theniterate over the given array and whatever value we find we make it value as one. then again iterate over our hased array and then whatever index has the value as 0 return that index. Here the complexity will be O(2N). the space complexity whereas is O(N). 

# here now we have two appraoch in optimal solution.

#sum apprach we can directly find the sum of first n natural numbers with the formula (n*(n+1))//2 and hence we we find the sum by iterating over array of using the sum function which give the overall complexity of O(N) and space complexity of O(1).
nums = list(map(int,input().split()))
n = len(nums)
suming = (n*(n+1))//2
print(suming - sum(nums))

# XOR appraoch if we take XOR or two same number we get the result as 0. and if take XOR or and number with zero we get the number itself now if we take the values from 1 to N and take thier XOR value in one varible and then take the XOR of all the element in the array and store in another variable now we take the XOR of these two varibles and we get the missing value as behind the scence its being calulated as suppose n = 3 and arr = [1,3] so XOR1 = 1^2^3 XOR2 = 1^3 and result seems like (1^1)(2)(3^3) hence = 0^2^0 = 2.

#now we can use two loops one to calculate XOR for 1 to N number and another for the array but it will become O(2N) complexity hence we gonna use only one for loop 

nums = list(map(int, input().split()))
n = len(nums)
xor1 = 0  
xor2 = 0
for i in range(n):
    xor2 = xor2 ^ nums[i]
    xor1 = xor1 ^ (i+1)
xor1 ^= (n+1)
print(xor1^xor2)

# Now XOR is slightly better in terms of space for large test cases like 10^5 as if we calculate the sum it will be 10^5 * (10^5 +1) hence a order or 10^10 we can store such values in integer in c++ hence we need long it wont take so much space difference but its slighly higher than XOR one because the max the varible there can store will be 10^5 only the given number only .