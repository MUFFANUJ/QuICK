#include <bits/stdc++.h>
using namespace std;



void action(int index,vector<int> arr, vector<int> &ds, int size,int sum,int s){
  if (index == size)
  {
    if(s == sum){
      for(auto it : ds){
      cout << it << " ";
    }
    cout << "\n";
    }
    return;
  }
  
  s += arr[index];
  ds.push_back(arr[index]);
  action(index+1,arr,ds,size,sum, s);
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

