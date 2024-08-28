n = int(input())
arr = list(map(int,input().split()))
np = int(input())
countArr = [0]*(maxSize) # max Size is the the max number that is allowed to be stored in the array provided. in Python it can be max 10^8 only in cpp inside the int main we can have 10^6 and at global declaration we an have int array space as 10^7. for cases above the range of 10^8 use dictionary or map in cpp to only store the numbers which are occuring and not just make a array of full size.
# map gives the elements in sorted order and has time complexity of O(log n) in all cases(best,average,worst) whereas underorder_map just the same thing but do not has elements in sorted order has time complexity of O(1) in (best,average) and O(n) in worst cases so at first we should always opt for underorder map and in case of any time limit exceed error use map there. 

# why does the unordered_map goes into worst case is due to collisions where internally everyone goes to the same memroy space of for example division method (division method is a method where we have a limited size of an array and we have to store more data so we we do number with %10 and put the number in the place of its result also here we have a linked list in every index with multple values chained together and stored this is called linear chaining which is sorted so we can search through it easily in minimal time) these hashing method is used interanlly. there are more methods for internal hashing like folding method and mad square method. hence the worst case can happend  in situations like these which are very rare.

# for map we can have anything as key like pair int string anything but in unordered_map we can only have individual datatype as key we can have things like pair<?,?>
for i in range(n):
  countArr[arr[i]] += 1
  
for i in range(np):
  print(countArr[int(input())])
  
# the complexity here is O(n) if we compute this one by one the complexity would have been O(X*n) where X is the number of inputs fow which we are checking the counts.