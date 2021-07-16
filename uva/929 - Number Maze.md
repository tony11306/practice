```c++
// 也是 dijkstra 裸題
#include <bits/stdc++.h>
using namespace std;
#define f first
#define s second
#define dbg1(x) cout<<"Dbg--> "<<'['<<#x<<':'<<x<<']'<<endl
#define dbg2(x,y) cout<<"Dbg--> "<<'['<<#x<<':'<<x<<' '<<#y<<':'<<y<<']'<<endl
#define dbg3(x,y,z) cout<<"Dbg--> "<<'['<<#x<<':'<<x<<' '<<#y<<':'<<y<<' '<<#z<<':'<<z<<']'<<endl

const int INF = 1 << 28;
int adj[4][2] = {{0, 1}, {1, 0}, {-1, 0}, {0, -1}};

struct Node
{   
    Node() {
    }
    int a = 0;
    int b = 0;
    int dis = INF;
    bool friend operator<(Node, Node);
};

bool operator<(Node n1, Node n2) {
    return n1.dis > n2.dis;
}

void solve() {
    int n, m;
    cin >> n >> m;
    vector<vector<Node>> cost(n, vector<Node>(m));
    vector<vector<int>> weight(n, vector<int>(m));
    vector<vector<bool>> visited(n, vector<bool>(m));
    for(int i = 0; i < n; ++i) {
        for(int j = 0; j < m ; ++j) {
            cin >> weight[i][j];
            cost[i][j].a = i;
            cost[i][j].b = j;
            visited[i][j] = false;
        }
    }

    priority_queue<Node> pq;
    cost[0][0].a = 0;
    cost[0][0].b = 0;
    cost[0][0].dis = weight[0][0];
    pq.push(cost[0][0]);

    while(!pq.empty()) {
        Node nd = pq.top();
        pq.pop();
        if(visited[nd.a][nd.b]) {
            continue;
        }
        visited[nd.a][nd.b] = true;
        
        for(int i = 0; i < 4; ++i) {
            if(nd.a+adj[i][0] >= n || nd.a+adj[i][0] < 0 || nd.b+adj[i][1] >= m || nd.b+adj[i][1] < 0) {
                continue;
            }
            if(cost[nd.a+adj[i][0]][nd.b+adj[i][1]].dis > cost[nd.a][nd.b].dis + weight[nd.a+adj[i][0]][nd.b+adj[i][1]]) {
                // dbg3(nd.a, nd.b, nd.dis);
                cost[nd.a+adj[i][0]][nd.b+adj[i][1]].dis = cost[nd.a][nd.b].dis + weight[nd.a+adj[i][0]][nd.b+adj[i][1]];
                if(!visited[nd.a+adj[i][0]][nd.b+adj[i][1]]) {
                    pq.push(cost[nd.a+adj[i][0]][nd.b+adj[i][1]]);
                }
            }
        }
    }
    cout << cost[n-1][m-1].dis << endl;
}

int main() {
    
    
    int n;
    cin >> n;
    while(n--) {
        solve();
    }

    system("pause");

    return 0;
}
```
