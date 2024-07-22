#include <iostream>
using namespace std;

int main()
{
    int size;
    cin >> size;
    for (int i = 1; i <= size; i++)
    {
        for (int j = 1; j <= i; j++)
        {
            cout << "*";
        }
        cout << "\n";
    }
    for (int i = size - 1; i >= 0; i--)
    {
        for (int j = 1; j <= i; j++)
        {
            cout << "*";
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
//     int start;
//     for (int i = 1; i <= 2*size-1; i++)
//     {
//       start = i;
//       if(start > size ) start = 2*size -i;
//       for (int j = 1; j <= start; j++)
//       {
//           cout << "*";
//       }
//       cout << "\n";
//     }

//     return 0;
// }