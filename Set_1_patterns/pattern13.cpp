#include <iostream>
using namespace std;

int main()
{
    int size;
    cin >> size;
    int value = 1;
    for (int i = 1; i <= size; i++)
    {
        for (int j = 1; j <= i; j++)
        {
            cout << value << " ";
            value++;
        }
        cout << "\n";
    }

    return 0;
}