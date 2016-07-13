#include <iostream>

using namespace std;

int main()
{
    int amount;
    while(cin >> amount && amount != 0)
    {
        int numbers = amount;
        int num;
        cin >> num;
        int last_num = num;
        int result = 0;
        if(num > 0)
            result = num * 6 + 5;
        else
            result = num * 4 + 5;
        numbers--;
        while(numbers)
        {
            cin >> num;
            if(num - last_num > 0)
                result = result + (num - last_num) * 6 + 5;
            else
                result = result + (last_num - num) * 4 + 5;
            last_num = num;
            numbers--;
        }
        cout << result << endl;
    }
    return 0;
}
