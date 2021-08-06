```c++
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

void printWave(int m) {
    for(int i = 1; i <= m; ++i) {
        for(int j = 0; j < i; ++j) {
            cout << i;
        }
        cout << endl;
    }
    for(int i = m-1; i >= 1; --i) {
        for(int j = 0; j < i; ++j) {
            cout << i;
        }
        cout << endl;
    }
}

void solve() {
    int n, m;
    cin >> n >> m;
    printWave(n);
    m--;
    while(m--) {
        cout << endl;
        printWave(n);
    }
}

int main() {
    int n;
    cin >> n;
    solve();
    n--;
    while(n--) {
        cout << endl;
        solve();
    }
    system("pause");
}
```
