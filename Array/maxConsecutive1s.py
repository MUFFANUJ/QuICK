#so there is not much in this problem for making brute better optimal we can directly use the optimal one having two varibles one who will keep the temp count of once and one which will store the max we go through the array if we find 1 we increment thr temp count varible and if we find 0 or anything then we find max of the max count and temp count and assign it to max count later make temp count 0  now before giving answer we check once again to make sure we didnt miss the last count 
 
# time complexity -> O(N) | space complexity -> O(1)
nums = list(map(int, input().split()))
count = 0
temp = 0
for i in nums:
    if i == 1:
        temp += 1
    else:
        count = max(count,temp)
        temp = 0
print(max(count,temp))