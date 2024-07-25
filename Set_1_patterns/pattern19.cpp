#include <iostream>
using namespace std;

int main()
{
    int size;
    cin >> size;
    for (int i = 0; i<size ; i++)
    { 
      for(int j = 1; j<= size-i;j++){
        cout << "* ";
      }
      for(int j = 1; j<= 2*i;j++){
        cout << "  ";
      }
      for(int j = 1; j<= size-i;j++){
        cout << "* ";
      }
      cout << "\n";
    }
    for (int i = 1; i<=size ; i++)
    { 
      for(int j = 1; j<= i;j++){
        cout << "* ";
      }
      for(int j = 1; j<= 2*size-2*i;j++){
        cout << "  ";
      }
      for(int j = 1; j<= i;j++){
        cout << "* ";
      }
      cout << "\n";
    }

    
    return 0;
}