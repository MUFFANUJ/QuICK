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