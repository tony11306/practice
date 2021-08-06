```c++
// 大一新生盃程式競賽的題目 當初看到只知道是dp但不會寫
// 現在終於會了 反正就是按右界排序後 dp[i]為第i個線段右界的最佳選擇 往前用O(n)找合法轉移
// 整體為O(n^2);
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

struct Advertisement {
    int floor;
    int covered;
    int price;
};

void solve() {
    int n;
    cin >> n;
    vector<Advertisement> ads;
    int ceiling = 0;
    for(int i = 0; i < n; ++i) {
        Advertisement adv;
        cin >> adv.floor >> adv.covered >> adv.price;
        ceiling = max(ceiling, adv.floor+adv.covered);
        ads.push_back(adv);
    }
    sort(ALL(ads), [&](const Advertisement& a, const Advertisement& b){
        if(a.floor == b.floor) {
            return a.covered < b.covered;
        }
        return a.floor+a.covered < b.floor+b.covered;
    });

    int dp[n];
    dp[0] = ads[0].price;
    for(int i = 1; i < n; ++i) {
        dp[i] = ads[i].price;
        for(int j = i-1; j >= 0; --j) {
            if(ads[j].covered + ads[j].floor - 1 >= ads[i].floor) {
                dp[i] = max(dp[i], dp[j]);
            } else if(ads[j].covered + ads[j].floor - 1 < ads[i].floor) {
                dp[i] = max(dp[i], ads[i].price + dp[j]);
                break;
            }
        }
    }

    cout << dp[n-1] << endl;
    
}

int main() {
    int n;
    cin >> n;
    FOR_EACH_CASE(n) {
        solve();
    }
    system("pause");
}
```
