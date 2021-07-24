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
int ans = 0;
void floydWarshall(vector<vector<int>>& graph) {
    int n = graph.size()-1;
    for(int k = 1; k <= n; ++k) {
        for(int i = 1; i <= n; ++i) {
            for(int j = 1; j <= n; ++j) {
                graph[i][j] = min(graph[i][k]+graph[k][j], graph[i][j]);
                ans = graph[i][j] != INF_0x3f ? max(ans, graph[i][j]) : ans;
            }
        }
    }
}

void solve(int n) {
    ans = 0;
    vector<vector<int>> origin(n+1, vector<int>(n+1, INF_0x3f));
    vector<vector<int>> proposal(n+1, vector<int>(n+1, INF_0x3f));
    for(int i = 1; i <= n; ++i) {
        string s;
        getline(cin, s);
        stringstream ss(s);
        int a;
        ss >> a;
        int b;
        origin[a][a] = 0;
        while(ss >> b) {
            origin[a][b] = 1;
        }
    }

    for(int i = 1; i <= n; ++i) {
        string s;
        getline(cin, s);
        stringstream ss(s);
        int a;
        ss >> a;
        int b;
        proposal[a][a] = 0;
        while(ss >> b) {
            proposal[a][b] = 1;
        }
    }
    int a, b;
    cin >> a >> b;
    floydWarshall(origin);
    floydWarshall(proposal);
    int flag = true;
    for(int i = 1; i <= n; ++i) {
        for(int j = 1; j <= n; ++j) {
            if(proposal[i][j] > origin[i][j]*a+b) {
                flag = false;
                break;
            }
        }
        if(!flag) {
            break;
        }
    }
    if(flag) {
        cout << "Yes\n";
    } else {
        cout << "No\n";
    }
    // cout << ans << endl;  Cpe modified.
}

int main() {
    int n;
    while(cin >> n && n != 0) {
        cin.get();
        solve(n);
    }
    system("pause");
}
```
