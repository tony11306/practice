```c++
// 找規律 然後分解出相同的子問題
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

void solve(int n) {
    while(n--) {
        int cur = 1;
        int d, k;
        cin >> d >> k;
        while(--d) {
            if(k%2 == 1 || k == 0) {
                cur *= 2;
                k = (k+1)/2;
            } else {
                cur = cur * 2 + 1;
                k /= 2;
            }
        }
        cout << cur << endl;
    }
}

int main() {
    int n;
    while(cin >> n && n != -1) {
        solve(n);
    }
    system("pause");
}

```
