#include <iostream>
using namespace std;

int main()
{
    int size;
    cin >> size;
    int start;
    for (int i = 0; i < size; i++)
    {
        if (i % 2 == 0)
            start = 1;
        else
            start = 0;
        for (int j = 0; j <= i; j++)
        {
            cout << start;
            start = 1 - start;
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
//     for (int i = 1; i <= size; i++)
//     {
//       if(i%2 == 1){
//           cout << "1 ";
//       }
//       for (int j = 1; j <= i/2; j++)
//       {
//         cout << "0 1 ";
//       }
//       cout << "\n";
//     }

//     return 0;
// }