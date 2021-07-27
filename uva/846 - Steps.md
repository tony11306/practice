```c++
// 純思維題，很像是 cf 會出的題目
// 123 12321 1234321 <=> 4 9 16
// 找規律
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

vector<ll> table;
void buildTable() {
    ll a = 1;
    while(a*a < INF) {
        table.push_back(a*a);
        a++;
    }
}

void solve() {
    int a;
    int b;
    cin >> a >> b;
    if(b-a <= 3) {
        cout << b - a << endl;
        return;
    }
    int s = b-a;
    auto it = lower_bound(table.begin(), table.end(), s)-1;
    if(s == *it) {
        cout << int((sqrt(s)-1)*2 + 1) << endl;
    } else {
        if(s - *it > sqrt(*it)) {
            cout << int((sqrt(*it)-1)*2 + 3) << endl;
        } else {
            cout << int((sqrt(*it)-1)*2 + 2) << endl;
        }
    }
}

int main() {
    buildTable();
    int n;
    cin >> n;
    while(n--) {
        solve();
    }
    
    system("pause");
}

```
