```c++
// ...?
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
    int sum = 0;
    for(int i = 1; i < n; ++i) {
        if(n % i == 0) {
            sum += i;
        }
    }
    if(sum > n) {
        cout << "abundant" << endl;
    } else if(sum < n) {
        cout << "deficient" << endl;
    } else {
        cout << "perfect" << endl;
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
