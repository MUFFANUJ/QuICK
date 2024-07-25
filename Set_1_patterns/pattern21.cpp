#include <iostream>
using namespace std;

int main()
{
    int size;
    cin >> size;
    if(size == 1){
      cout << "*";
    }else {
      for (int i = 0; i<size ; i++)
    { 
      cout << "*";
    }
    
    cout<<"\n";
    
    for (int i = 0; i<size-2 ; i++)
    { 
      cout << "*";
      for (int i = 0; i<size-2 ; i++)
      { 
        cout << " ";
      }
      cout << "*";
      cout<<"\n";
    }
    
    for (int i = 0; i<size ; i++)
    { 
      cout << "*";
    
    }
    }

    
    return 0;
}