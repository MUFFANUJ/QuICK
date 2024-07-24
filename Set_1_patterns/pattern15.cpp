#include <iostream>
using namespace std;

int main()
{
    int size;
    cin >> size;
    
    for (int i = size; i >= 1; i--)
    {
      for(char j ='A';j<'A'+i;j++){
       cout << j << " ";
      }
      cout << "\n";
    }
    
    return 0;
}