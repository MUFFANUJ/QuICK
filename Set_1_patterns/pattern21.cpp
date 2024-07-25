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



// #include <iostream>
// using namespace std;

// int main()
// {
//     int size;
//     cin >> size;
//     for (int i = 0; i < size; i++)
//     {
//       //spaces
//         for (int j = 0; j < size; j++)
//         {
//           if(i == 0 || j == 0 || i == size-1|| j == size-1) cout << "*";
//           else cout << " ";
//         }
        
//         cout << "\n";
//     }
//     return 0;
// }