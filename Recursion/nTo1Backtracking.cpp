#include <iostream>
using namespace std;


void back(int i,int n){
  if (i>n) return;
  back(i+1,n); // as the function call is first hence the states for cout will be executes only once the base condition is met
  std::cout << i << std::endl;
}
int main() 
{
    int size;
    cin >> size;
    back(1,size);
    return 0;
}