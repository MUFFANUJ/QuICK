#include <iostream>
using namespace std;

int main()
{
    int size;
    cin >> size;
    for (int i = 0; i < 2*size-1; i++)
    {
        for (int j = 0; j < 2*size-1; j++)
        {
          int top = i;
          int bottom = 2*size-2 -i;
          int left = j;
          int right = 2*size-2 - j;
          cout << size - min(min(top,bottom),min(left,right));
        }
        cout << "\n";
    }
    return 0;
}