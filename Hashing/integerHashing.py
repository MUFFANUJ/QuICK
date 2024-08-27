n = int(input())
arr = list(map(int,input().split()))
np = int(input())
countArr = [0]*(maxSize) # max Size is the the max number that is allowed to be stored in the array provided. in Python it can be max 10^8 only in cpp inside the int main we can have 10^6 and at global declaration we an have int array space as 10^7.
for i in range(n):
  countArr[arr[i]] += 1
  
for i in range(np):
  print(countArr[int(input())])
  
# the complexity here is O(n) if we compute this one by one the complexity would have been O(X*n) where X is the number of inputs fow which we are checking the counts.