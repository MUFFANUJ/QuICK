#include <iostream>
#include <string>
using namespace std;

int main()
{
    int size;
    cin >> size;
    for (int i = 1; i <= size; i++)
    {
        for (int j = 1; j <= i; j++)
        {
            cout << i << " ";
        }
        cout << "\n";
    }
    return 0;
}