#the approach used in the previous problem wont work here because there can be some edge cases where the 
#start mid and end postion value are the same for example - arr = [3,1,2,3,3,3,3] so here we cant compare 
#or find which part is sorted programmatically (also we cant find the index or target element in this case using binary 
#search we have to use linear search only) -> question made using this would be to find if the element exist in this or not


# the solution for this problem is to trim down the search space everytime we find arr[low] = arr[mid] = arr[high]
# hence trimming the search space will at some point bring me to the point where i might be able to compare and find the sorted area.