#include <iostream>
using namespace std;

int main()
{
    int size;
    cin >> size;
    
    for (int i = 1; i <= size; i++)
    {
      for(int j =1;j<=2*size-2*i;j++){
       cout << " ";
      }
      int start = 1;
      char value = '@';
      for(int j = 1;j<=2*i-1;j++){
        if((2*i)/2+1 <= j) value = value -1;
        else value = '@' + j;
        cout << value << " ";
      }
      cout << "\n";
    }
    
    return 0;
}