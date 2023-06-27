#include <iostream>
#include <string>       
#include <vector>         
#include <algorithm>    

using namespace std;

string arr[21000];

bool cmp(const string& a, const string& b){                   
    if (a.size() == b.size()) return a < b;
    return a.size() < b.size();
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);

    int i, j;
    int n; cin >> n;

    for (i = 0;i < n;i++)
        cin >> arr[i];

    sort(arr, arr + n, cmp);                  
   
    for (i = 0;i < n;i++)
    {   
        if (arr[i] != arr[i + 1])
            cout << arr[i] << "\n";
    }
    return 0;
}