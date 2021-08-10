```c++
// 一次過耶 :D，就 dfs 或 bfs 而已
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

struct Node {
    char color = 'N';
    vector<int> adj;
};

int edges;
int n;

void solve() {
    Node g[n];
    for(int i = 0; i < edges; ++i) {
        int a, b;
        cin >> a >> b;
        g[a].adj.push_back(b);
        g[b].adj.push_back(a);
    }
    int visited[n] = {false};
    queue<int> q;
    q.push(0);
    g[0].color = 'W';
    bool isBio = true;
    while(!q.empty() && isBio) {
        int node = q.front();
        visited[node] = true;
        for(int adj : g[node].adj) {
            if(g[adj].color != 'N') {
                if(g[adj].color == g[node].color) {
                    isBio = false;
                    break;
                }
            } else {
                if(g[node].color == 'W') {
                    g[adj].color = 'B';
                } else {
                    g[adj].color = 'W';
                }
            }

            if(!visited[adj]) {
                q.push(adj);
            }
            
        }
        q.pop();
    }

    if(isBio) {
        cout << "BICOLORABLE." << endl;
    } else {
        cout << "NOT BICOLORABLE." << endl;
    }
    

}

int main() {
    while(cin >> n >> edges) {
        solve(); 
    }
}
```
