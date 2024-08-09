// while counting just return 1 when the base condition is met and return 0 when not and at the end return ths ummation for all recursive calls 

#include <bits/stdc++.h>
using namespace std;



int action(int index,vector<int> arr, int size,int sum,int s){
  if (index == size)
  {
    if(s == sum){
      return 1;
    }
    return 0;
  }
  
  s += arr[index];
  int l = action(index+1,arr,size,sum, s);
  s -= arr[index];
  int r = action(index+1,arr,size,sum,s);
  return l+r;
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

    cout << action(0,vec,n,sum,0);
    return 0;
}

