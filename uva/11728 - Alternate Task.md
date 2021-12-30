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

int table[1001];

int main() {
    
    for(int i = 1; i < 1001; ++i) {
        for(int j = 1; i*j < 1001; ++j) {
            table[i*j] += i;
        }
    }
    map<int, int> mp;
    for(int i = 0; i < 1001; ++i) {
        mp[table[i]] = i;
    }

    int n;
    FOR_EACH_CASE(INF && cin >> n && n != 0) {
        if(mp.find(n) != mp.end()) {
            cout << mp[n] << endl;
        } else {
            cout << -1 << endl;
        }
    }
    system("pause");
}
```
