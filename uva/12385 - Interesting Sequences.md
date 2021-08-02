```c++
// 這題就簡單dp而已
// 這是優化過的
// 我用沒優化過的uva-AC zj-TLE
// 就知道 uva 測資多弱...
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

void solve() {
    int n;
    cin >> n;
    int dp[n+1] = {0};
    int mp[100001] = {0};

    for(int i = 1; i <= n; ++i) {
        int a;
        cin >> a;
        if(mp[a] == 0) {
            mp[a] = i;
            dp[i] = dp[i-1];
        } else {
            dp[i] = max({dp[mp[a]]+1, dp[i], dp[i-1]});     
        }
        mp[a] = i;
        
    }
    cout << dp[n] << endl;
}

int main() {
    int n;
    cin >> n;
    while(n--) {
        solve();
    }
    system("pause");
}

```
