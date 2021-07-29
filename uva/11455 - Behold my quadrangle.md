```c++
#include<bits/stdc++.h>
#define ll long long
#define endl "\n"
#define dbg1(x) cout<<"Dbg--> "<<'['<<#x<<':'<<x<<']'<<endl
#define dbg2(x,y) cout<<"Dbg--> "<<'['<<#x<<':'<<x<<' '<<#y<<':'<<y<<']'<<endl
#define dbg3(x,y,z) cout<<"Dbg--> "<<'['<<#x<<':'<<x<<' '<<#y<<':'<<y<<' '<<#z<<':'<<z<<']'<<endl
#define FOR_EACH_CASE(x) for(int cas = 1; cas <= x && (cout << "Case " << cas << ": "); ++cas)
#define iss std::ios::sync_with_stdio(0);std::cin.tie(0)
using namespace std;
const int INF = ~(1<<31);
const int INF_0x3f = 0x3f3f3f3f;



int main() {
    
    int n;
    cin >> n;
    while(n--) {
        int arr[4];
        for(int i = 0; i < 4; ++i) {
            cin >> arr[i];
        }
        sort(arr, arr+4);
        if(arr[0] == arr[1] && arr[1] == arr[2] && arr[2] == arr[3]) {
            cout << "square" << endl;
        } else if(arr[0] == arr[1] && arr[2] == arr[3]) {
            cout << "rectangle" << endl;
        } else if(arr[0]+arr[1]+arr[2] > arr[3]) {
            cout << "quadrangle" << endl;
        } else {
            cout << "banana" << endl;
        }
    }
    system("pause");
}

```
