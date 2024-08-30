# if we see the brute force approach in this it will be just sort the given array and return the value at last index because as array is sorted the last element will be the max but the minimum time complexity for doing sort will be O(n * log n) hence its not optimal the optimal solution will be to declare a varible with initial value as first value and run a loop from 1st value to end or array and if we find any value larger than the value stores in the varible we will change the its value and store in the varible and at last the varible will have the maximum value 

largest = arr[0]
for i in range(1,len(arr)):
  if largest < arr[i]:
    largest = arr[i]
print(largest)