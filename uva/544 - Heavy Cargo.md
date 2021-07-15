```c++
// Dijkstra 或 Bellman-Ford 應該都可以
// 我只會 dijkstra
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

void test(priority_queue<pair<int, string>, vector<pair<int, string>>, less<pair<int, string>>> pq) {
    cout << "----test----" << endl;
    while(!pq.empty()) {
        cout << pq.top().second << " " << pq.top().first << endl;
        pq.pop();
    }
}

void solve(int roadNum) {
    map<string, map<string, int>> edges;
    map<string, map<string, int>> dijkstra;
    set<string> cities;
    for(int i = 0; i < roadNum; ++i) {
        string from;
        string to;
        int weight;
        cin >> from >> to >> weight;
        edges[from][to] = max(weight, edges[from][to]);
        edges[to][from] = edges[from][to];
        cities.insert(from);
        cities.insert(to); 
        
        
    }

    string from, to;
    cin >> from >> to;
    // dijkstra
    map<string, bool> visited;
    priority_queue<pair<int, string>, vector<pair<int, string>>, less<pair<int, string>>> pq;

    for(auto start : cities) {
        for(auto end : cities) {
            if(start == end) {
                dijkstra[start][end] = 0;
                dijkstra[end][start] = 0;
            } else {
                dijkstra[start][end] = INF;
                dijkstra[end][start] = INF;
            }
        }
    }
    for(auto it = edges[from].begin(); it != edges[from].end(); ++it) {
        pq.push(make_pair(it->second, it->first));
    }
    visited[from] = true;
    while(!pq.empty()) {
        string current = pq.top().second;
        int prevWeight = pq.top().first;
        pq.pop();
        if(visited[current]) {
           continue; 
        } else {
            visited[current] = true;
        }
        
        dijkstra[from][current] = min(dijkstra[from][current], prevWeight);
        dijkstra[current][from] = dijkstra[from][current];
        if(current == to) {
            break;
        }

        for(auto it = edges[current].begin(); it != edges[current].end(); ++it) {
            pq.push(make_pair(min(edges[current][it->first], dijkstra[from][current]), it->first));
        }
    }

    cout << dijkstra[from][to] << " tons" << endl;


}

int main() {
    int n, m;
    int cas = 1;
    while(cin >> n >> m) {
        if(n == 0 && m == 0) {
            break;
        }
        cout << "Scenario #" << cas << endl;
        solve(m);
        cas++;
        cout << endl;
    }
    system("pause");
}
```
