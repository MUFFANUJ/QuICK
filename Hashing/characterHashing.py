n = int(input())
arr = list(map(str,input().split()))
np = int(input())
countArr = [0]*(26) # initailizing with the 26 alphabets assuming only lower cases here. if we had to simplify this and we had more characters here we could have taken a 256 character array where we can directly on index level directly assign values like interger one.
for i in range(n):
  countArr[ord(arr[i]) -ord("a")] += 1 # 'f' - 'a' will give the array index 102-97 = 5 so here we are adding on the particular array index 
  
for i in range(np):
  print(countArr[(ord(input()) - ord('a'))]) # here just calling back the index 
  