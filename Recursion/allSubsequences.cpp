// using btake or not take
// timeComplexity = O(n*2^n)
//spaceComplexity = O(n)
#include <bits/stdc++.h>
using namespace std;



void action(int index,vector<int> arr, vector<int> &ds, int size){
  if (index == size)
  {
    for(auto it : ds){
      cout << it << " ";
    }
    cout << "\n";
    return;
  }
  
  ds.push_back(arr[index]);
  action(index+1,arr,ds,size);
  ds.pop_back();
  action(index+1,arr,ds,size);
}


int main() 
{
    int n;
    cin >> n;
    vector<int> vec(n);
    for(int i = 0; i < n; ++i) {
        cin >> vec[i];  
    }
    
    vector<int> ds;
    action(0,vec,ds,n);
    return 0;
}

