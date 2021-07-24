```c++
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

vector<pair<int, int>> table(1000001, pair<int, int>(2, 0));

void buildTable() {
    int tmp = 0;
    int ans = 1;
    for(int i = 1; i <= 1000000; ++i) {
        for(int j = 2; i*j <= 1000000; ++j) {
            table[i*j].first++;
        }
        if(table[i].first >= tmp) {
            tmp = table[i].first;
            ans = i;
        }
        table[i].second = ans;
    }
}

void solve() {
    int n;
    cin >> n;
    cout << table[n].second << endl;
}

int main() {
    int n;
    buildTable();
    cin >> n;
    while(n--) {
        solve();
    }
    system("pause");
}
```
