#include <iostream>

using namespace std;

int main()
{
    int arr[60];
    long long a, b, n;
    arr[0] = arr[1] = arr[2] = 1;
    while(cin >> a >> b >> n)
    {
        if(a == 0 && b == 0 && n == 0)
            break;
        int arr_begin, arr_end, flag = 0;
        for( int i = 3; i <= n && !flag; ++i )
        {
            arr[i] = ( a * arr[i-1] + b * arr[i-2] ) % 7;
            for( int j = 2; j <= i - 1; ++j )
            {
                if( arr[i] == arr[j] && arr[i-1] == arr[j-1] )
                {
                    arr_begin = j, arr_end = i;
                    flag = 1;
                    break;
                }
            }
        }
        if( flag )
        {
            cout << arr[arr_begin+(n-arr_end)%(arr_end-arr_begin)] << endl;
        }
        else
            cout << arr[n] << endl;

    }
    return 0;
}
