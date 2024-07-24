#include <iostream>
using namespace std;

int main()
{
    int size;
    cin >> size;
    
    for (int i = 1 ; i <= size; i++)
    {
      char value = '@' + i;
      for(char j =0;j<i;j++){
       cout << value << " ";
      }
      cout << "\n";
    }
    
    return 0;
}