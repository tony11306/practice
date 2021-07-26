```c++
// 我這題丟到 zj 會 tle
// 這題正解應該用 dp 解
// 只是測資很弱 而且同餘定理可以壓時間
// uva 1.3s 壓過去了...
// 算假解嗎?
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

void solve() {
    vector<set<int>> vt(10000);
    int n, k;
    cin >> n >> k;
    for(int i = 0; i < n; ++i) {
        int a;
        cin >> a;
        if(i == 0) {
            vt[i].insert(a);
        } else {
            for(int val : vt[i-1]) {
                vt[i].insert((val+a)%k);
                vt[i].insert((val-a)%k);
            }
        }
    }
    if(n == 1) {
        if(*vt[0].begin() % k == 0) {
            cout << "Divisible" << endl;
        } else {
            cout << "Not divisible" << endl;
        }
    } else if(vt[n-1].find(0) != vt[n-1].end()) {
        cout << "Divisible" << endl;
    } else {
        cout << "Not divisible" << endl;
    }
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
