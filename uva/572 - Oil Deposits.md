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


int n, m;
vector<vector<char>> g;
vector<vector<bool>> visited;
void dfs(int i, int j) {
    if(visited[i][j] || g[i][j] == '*') {
        return;
    }
    visited[i][j] = true;
    for(int k = i-1; k <= i+1; ++k) {
        for(int h = j-1; h <= j+1; ++h) {
            if(k >= 0 && k < n && h >= 0 && h < m) {
                dfs(k, h);
            }
        }
    }
}

void solve() {
    g = vector<vector<char>>(n, vector<char>(m));
    visited = vector<vector<bool>>(n, vector<bool>(m, false));
    for(int i = 0; i < n; ++i) {
        for(int j = 0; j < m; ++j) {
            cin >> g[i][j];
        }
    }
    int ans = 0;
    for(int i = 0; i < n; ++i) {
        for(int j = 0; j < m; ++j) {
            if(!visited[i][j]) {
                if(g[i][j] == '@') {
                    ans++;
                    dfs(i, j);
                } else {
                    visited[i][j] = true;
                }
            }
        }
    }
    cout << ans << endl;
}

int main() {
    while(cin >> n >> m && n != 0 && m != 0) {
        solve();
    }
    system("pause");
}
```
