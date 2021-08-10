```c++
// 經典 dp 問題，itsa 考過但我不會，現在大概懂了(嗎
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
    string s;
    getline(cin, s);
    stringstream ss(s);
    vector<int> arr;
    int a;
    int sum = 0;
    while(ss >> a) {
        arr.push_back(a);
        sum += a;
    }
    if(sum % 2 != 0) {
        cout << "NO" << endl;
        return;
    }
    sort(ALL(arr));

    int weight = sum/2;
    int dp[weight + 1] = {0};

    for(int w : arr) {
        for(int i = weight; i >= w; --i) {
            if(w <= i) {
                dp[i] = max(dp[i], dp[i-w] + w);
            }
        }
    }

    if(dp[weight] == weight) {
        cout << "YES" << endl;
    } else {
        cout << "NO" << endl;
    }

}

int main() {
    int n;
    cin >> n;
    cin.get();
    while(n--) {
        solve();
    }
    system("pause");
}
```
