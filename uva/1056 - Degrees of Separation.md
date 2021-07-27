```c++
// floyd-warshall 裸題...
// 完全套模板就可以了
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

void floydWarshall(vector<vector<int>>& g) {
    int siz = g.size();
    for(int k = 0; k < siz; ++k) {
        for(int i = 0; i < siz; ++i) {
            for(int j = 0; j < siz; ++j) {
                g[i][j] = min(g[i][k]+g[k][j], g[i][j]);
            }
        }
    }
}

void solve(int a, int b) {
    map<string, int> ids;
    vector<vector<int>> g(a, vector<int>(a, INF_0x3f));
    while(b--) {
        string s1, s2;
        cin >> s1 >> s2;
        if(ids.find(s1) == ids.end()) {
            ids.insert({s1, ids.size()});
            g[ids[s1]][ids[s1]] = 0;
        }
        if(ids.find(s2) == ids.end()) {
            ids.insert({s2, ids.size()});
            g[ids[s2]][ids[s2]] = 0;
        }
        g[ids[s1]][ids[s2]] = 1;
        g[ids[s2]][ids[s1]] = 1;
    }

    floydWarshall(g);
    int ans = 0;
    for(auto vt : g) {
        for(int val : vt) {
            ans = max(val, ans);
        }
    }

    if(ans == INF_0x3f) {
        cout << "DISCONNECTED" << endl;
    } else {
        cout << ans << endl;
    }

}

int main() {
    int cas = 1;
    int a, b;
    while(cin >> a >> b && a != 0 && b != 0 && cout << "Network " << cas << ": ") {
        cas++;
        solve(a, b);
        cout << endl;
    }
    system("pause");
}

```
