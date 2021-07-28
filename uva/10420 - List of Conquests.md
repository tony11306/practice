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

void solve(int n) {
    map<string, int> mp;
    cin.get();
    while(n--) {
        string s;
        getline(cin, s);
        stringstream ss(s);
        ss >> s;
        mp[s]++;
    }
    for(auto it : mp) {
        cout << it.first << " " << it.second << endl;
    }
}

int main() {
    
    int n;
    cin >> n;
    solve(n);
    while(cin >> n) {
        cout << endl;
        solve(n);
    }
    system("pause");
}

```
