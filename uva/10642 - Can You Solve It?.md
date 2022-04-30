```c++
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

ll seq[100001];
void buildSeq() {
    for(int i = 1; i <= 100000; ++i) {
        seq[i] = seq[i-1] + i;
    }
}

void solve() {
    ll x1, y1, x2, y2;
    cin >> x1 >> y1 >> x2 >> y2;

    cout << abs((seq[y1] + ((y1+2) * x1) + (x1 * (x1 - 1)) / 2)  - (seq[y2] + ((y2+2) * x2) + (x2 * (x2 - 1)) / 2))<< endl;
}

int main() {
    buildSeq();
    int n;
    cin >> n;
    FOR_EACH_CASE(n) {
        solve();
    }
    system("pause");
}
```
