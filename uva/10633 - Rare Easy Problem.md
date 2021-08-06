```c++
// 我邏輯不好 直接數學推回去
// 發現 ll 會烙賽 那就開 unsigned ll
// 爽辣
#include<bits/stdc++.h>
#define ll long long
#define endl "\n"
#define dbg1(x) cout<<"Dbg--> "<<'['<<#x<<':'<<x<<']'<<endl
#define dbg2(x,y) cout<<"Dbg--> "<<'['<<#x<<':'<<x<<' '<<#y<<':'<<y<<']'<<endl
#define dbg3(x,y,z) cout<<"Dbg--> "<<'['<<#x<<':'<<x<<' '<<#y<<':'<<y<<' '<<#z<<':'<<z<<']'<<endl
#define ALL(x) x.begin(), x.end()
#define FOR_EACH_CASE(x) for(int cas = 1; cas <= x && (cout << "Case " << cas << ": "); ++cas)
#define iss std::ios::sync_with_stdio(0);std::cin.tie(0)
using namespace std;
const int INF = ~(1<<31);
const int INF_0x3f = 0x3f3f3f3f;

void solve(unsigned ll n) {
    ll a, b, c;
    a = n*10/9;
    b = a+1;
    c = a-1;
    bool flag = false;
    if(c - c/10 == n) {
        cout << c;
        flag = true;
    }

    if(a - a/10 == n) {
        if(flag) {
            cout << " ";
        }
        flag = true;
        cout << a;
    }

    if(b - b/10 == n) {
        if(flag) {
            cout << " ";
        }
        cout << b;
    }
    cout << endl;
    
}

// n - floor(n/10) = k;
// n = k + (n/10)
// 10n = 10k + n
// 9n = 10k;

int main() {
    ll n;
    while(cin >> n && n != 0) {
        solve(n);
    }
    system("pause");
}
```
