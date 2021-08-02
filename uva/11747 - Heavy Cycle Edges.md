```c++
// 第一次寫最小生成樹題目
// 大概認識了 kruskal 演算法，並簡單實作了並查集
// 這題題目大概就是找最小生成樹以外的邊而已
// 就算不是最小生成樹 只要用 kruskal 過程中有去掉 都要輸出
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

struct Edge {
    int from;
    int to;
    int weight;
};

int find(int* parent, int n, int node) {
    int current = node;
    while(parent[current] != -1) {
        current = parent[current];
    }
    return current;
}

bool isSameSet(int* parent, int n, int a, int b) {
    return find(parent, n, a) == find(parent, n, b);
}

void merge(int* parent, int n, int a, int b) {
    int rootA = find(parent, n, a);
    int rootB = find(parent, n, b);
    if(rootA != rootB) {
        parent[rootA] = rootB;
    }
}

void solve(int n, int m) {
    vector<int> ans;
    vector<Edge> edges;
    int parent[n];
    memset(parent, -1, sizeof(parent));
    while(m--) {
        Edge edge;
        cin >> edge.from >> edge.to >> edge.weight;
        edges.push_back(edge);
    }
    sort(edges.begin(), edges.end(), [&](Edge& a, Edge& b){
        return a.weight < b.weight;
    });
    
    for(Edge& edge : edges) {
        if(!isSameSet(parent, n, edge.from, edge.to)) {
            merge(parent, n, edge.from, edge.to);
        } else {
            ans.push_back(edge.weight);
        }
    }

    if(ans.size() == 0) {
        cout << "forest" << endl;
        return;
    }

    for(int i = 0; i < ans.size(); ++i) {
        if(i == 0) {
            cout << ans[i];
        } else {
            cout << " " << ans[i];
        }
    }
    cout << endl;
}

int main() {
    int n, m;
    while(cin >> n >> m) {
        if(n == 0 && m == 0) {
            break;
        }
        solve(n, m);
    }
    system("pause");
}

```
