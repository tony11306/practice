```c++
// dp problem
#include<bits/stdc++.h>
#define ll long long
#define endl "\n"
#define dbg1(x) cout<<"Dbg--> "<<'['<<#x<<':'<<x<<']'<<endl
#define dbg2(x,y) cout<<"Dbg--> "<<'['<<#x<<':'<<x<<' '<<#y<<':'<<y<<']'<<endl
#define dbg3(x,y,z) cout<<"Dbg--> "<<'['<<#x<<':'<<x<<' '<<#y<<':'<<y<<' '<<#z<<':'<<z<<']'<<endl
#define ALL(x) x.begin(), x.end()
#define FOR_EACH_CASE(x) for(int cas = 1; cas <= x && (cout << "Case #" << cas << ": "); ++cas)
#define iss std::ios::sync_with_stdio(0);std::cin.tie(0)
using namespace std;
const int INF = ~(1<<31);
const int INF_0x3f = 0x3f3f3f3f;


int main() {
    ll dp[7490] = {};

    // 1 cent
    for(int i = 0; i < 7490; ++i) {
        dp[i] = 1;
    }

    // 5 cent
    for(int i = 5; i < 7490; ++i) {
        dp[i] += dp[i-5];
    }

    // 10 cent
    for(int i = 10; i < 7490; ++i) {
        dp[i] += dp[i-10];
    }

    // 25 cent
    for(int i = 25; i < 7490; ++i) {
        dp[i] += dp[i-25];
    }

    // 50 cent
    for(int i = 50; i < 7490; ++i) {
        dp[i] += dp[i-50];
    }

    int n;
    while(cin >> n) {
        cout << dp[n] << endl;
    }

    system("pause");
}

```
