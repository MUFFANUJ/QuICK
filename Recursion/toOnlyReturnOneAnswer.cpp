// Everytime when we want to return only one answer either we can keep a flag to and use it to detect and once the answer is reached use it to pass the execution but that will still make the other recursion calls hence alwyas return true when reached the base case and check on the function call if the function call returns true exit the the function~

#include <bits/stdc++.h>
using namespace std;



bool action(int index,vector<int> arr, vector<int> &ds, int size,int sum,int s){
  if (index == size)
  {
    if(s == sum){
      for(auto it : ds){
      cout << it << " ";
    }
    cout << "\n";
    return true;  // return true when the condition is met for the first time
    }
    return false;
  }
  
  s += arr[index];
  ds.push_back(arr[index]);
  if(action(index+1,arr,ds,size,sum, s)){
    return true;  // exit the function when the condition is met for the first time
  }
  s -= arr[index];
  ds.pop_back();
  action(index+1,arr,ds,size,sum,s);
}


int main() 
{
    int n;
    cin >> n;
    int sum;
    cin >> sum;
    vector<int> vec(n);
    for(int i = 0; i < n; ++i) {
        cin >> vec[i];  
    }
    
    vector<int> ds;
    action(0,vec,ds,n,sum,0);
    return 0;
}

