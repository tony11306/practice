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


void solve() {
    int m, y, c;
    cin >> m >> y >> c;
    string s;
    cin >> s;
    for(char c1 : s) {
        if(c1 == 'M') {
            m--;
        } else if(c1 == 'Y') {
            y--;
        } else if(c1 == 'C') {
            c--;
        } else if(c1 == 'R') {
            m--;
            y--;
        } else if(c1 == 'G') {
            y--;
            c--;
        } else if(c1 == 'V') {
            m--;
            c--;
        } else if(c1 == 'B') {
            m--;
            y--;
            c--;
        }

        if(m < 0 || y < 0 || c < 0) {
            cout << "NO" << endl;
            return;
        }
    }
    cout << "YES " << m << ' ' << y << ' ' << c << endl;
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
