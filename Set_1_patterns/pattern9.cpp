#include <iostream>
using namespace std;

int main()
{
    int size;
    cin >> size;
    for (int i = 0; i < size; i++)
    {
        for (int j = 1; j <= size - i - 1; j++)
        {
            cout << " ";
        }
        for (int j = 1; j <= 2 * i + 1; j++)
        {
            cout << "*";
        }
        cout << "\n";
    }
    for (int i = size - 1; i >= 0; i--)
    {
        for (int j = 1; j <= size - i - 1; j++)
        {
            cout << " ";
        }
        for (int j = 1; j <= 2 * i + 1; j++)
        {
            cout << "*";
        }
        cout << "\n";
    }
    return 0;
}