#include <iostream>
using namespace std;

int main()
{
    int size;
    cin >> size;
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
    
    for (int i = size-1; i>=1 ; i--)
    { 
      for(int j = i; j>= 1;j--){
        cout << "* ";
      }
      for(int j = 1; j<= 2*size-2*i;j++){
        cout << "  ";
      }
      for(int j = i; j>= 1;j--){
        cout << "* ";
      }
      cout << "\n";
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