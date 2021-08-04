```c++
// 馬的 吃了一堆 runtime error
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

int n, m;

void solve() {
    vector<long> arr(n);
    for(int i = 0; i < n; ++i) {
        cin >> arr[i];
    }

    sort(ALL(arr), [&](long a, long b){
        if(a % m != b % m) {
            return (a % m) < (b % m);
        }
        
        if((a % 2) == 0 && (b % 2) == 0) {
            return a < b;
        } else if((a % 2) != 0 && (b % 2) != 0) {
            return b < a;
        } else {
            return abs(a % 2) == 1;
        }
    });

    cout << n << " " << m << endl;
    for(int i = 0; i < n; ++i) {
        cout << arr[i] << endl;
    }

}

int main() {
    while(cin >> n >> m) {
        if(n == 0 && m == 0) {
            break;
        }
        solve();
    }
    cout << 0 << " " << 0 << endl;
    system("pause");
}

```
