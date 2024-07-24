#include <iostream>
using namespace std;

int main()
{
    int size;
    cin >> size;
    for (int i = 1; i<=size ; i++)
    { 
      char value = '@' + size;
      for(int j = 1;j<=i;j++){
        cout << value << " ";
        value = value - 1;
      }
      cout << "\n";
    }
    
    return 0;
}