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

int n, m;
void solve() {

    if(n == 0 || m == 0) {
        cout << 0;
        return;
    }

    if(n == 1 || m == 1) {
        cout << max(n, m);
        return;
    }

    if(n == 2 && m == 2) {
        cout << 4;
        return;
    }

    if(n == 2 || m == 2) {
        cout << ((n*m) / 8)*4 + ((n*m)%8 >= 4 ? 4 : (n*m)%8);
        return;
    }

    cout << ((n*m)+1) / 2;

}

int main() {
    while(cin >> n >> m) {
        if(n == 0 && m == 0) {
            break;
        }
        solve();
        cout << " knights may be placed on a " << n << " row " << m << " column board." << endl;
    }
    system("pause");
}

```
