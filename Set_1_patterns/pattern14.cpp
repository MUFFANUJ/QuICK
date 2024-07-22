#include <iostream>
using namespace std;

int main()
{
    int size;
    cin >> size;

    for (int i = 1; i <= size; i++)
    {
        int AsciiValue = 65;
        for (int j = 1; j <= i; j++)
        {
            char value = static_cast<char>(AsciiValue);
            cout << value << " ";
            AsciiValue++;
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
//       for(char j ='A';j<'A'+i;j++){
//        cout << j << " ";
//       }
//       cout << "\n";
//     }

//     return 0;
// }