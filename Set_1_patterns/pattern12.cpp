#include <iostream>
using namespace std;

int main()
{
    int size;
    cin >> size;
    // alternatively define space for the first move and then make the change it needs for next iteration.
    for (int i = 1; i <= size; i++)
    {
        for (int j = 1; j <= i; j++)
        {
            cout << j;
        }
        for (int k = 1; k < 2 * size - 2 * i + 1; k++)
        {
            // cout<<i;
            cout << " ";
        }
        for (int s = i; s >= 1; s--)
        {
            cout << s;
        }
        cout << "\n";
        // space -+= something
    }

    return 0;
}