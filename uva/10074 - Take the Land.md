Largest square in a histogram的加強版，滿經典的stack演算法。

Took me couple hours to understand the stack method -.-||
```c++
#include<bits/stdc++.h>
#define ll long long
#define endl "\n"
#define dbg1(x) cout<<"Dbg--> "<<'['<<#x<<':'<<x<<']'<<endl
#define dbg2(x,y) cout<<"Dbg--> "<<'['<<#x<<':'<<x<<' '<<#y<<':'<<y<<']'<<endl
#define dbg3(x,y,z) cout<<"Dbg--> "<<'['<<#x<<':'<<x<<' '<<#y<<':'<<y<<' '<<#z<<':'<<z<<']'<<endl
#define ALL(x) x.begin(), x.end()
#define FOR_EACH_CASE(x) for(int cas = 1; cas <= x && (cout << "Case #" << cas << ": "); ++cas)
#define iss std::ios::sync_with_stdio(0);std::cin.tie(0)
using namespace std;
const int INF = ~(1<<31);
const int INF_0x3f = 0x3f3f3f3f;

int largestRectangle(int* row, int m) {
    stack<int> pos;
    stack<int> height;
    int ans = 0;

    pos.push(0);
    height.push(row[0]);

    for(int i = 1; i < m; ++i) {
        int tmp = i;
        if(row[i] < height.top()) {
            while(!height.empty() && height.top() > row[i]) {
                ans = max(ans, (i-pos.top())*height.top());
                tmp = pos.top();
                height.pop();
                pos.pop();
            }            
        }
        height.push(row[i]);
        pos.push(tmp);
        
    }

    while(!height.empty()) {
        ans = max(ans, (m-pos.top())*height.top());
        height.pop();
        pos.pop();
    }

    return ans;

}

void solve(int n, int m) {
    int row[m];
    int ans = 0;
    memset(row, 0, sizeof(row));

    for(int i = 0; i < n; ++i) {
        int t;
        for(int j = 0; j < m; ++j) {
            cin >> t;
            if(t == 0) {
                row[j]++;
            } else {
                row[j] = 0;
            }
        }
        ans = max(ans, largestRectangle(row, m));
    }

    cout << ans << endl;

}

int main() {
    int n, m;
    while(cin >> n >> m) {
        if(!(n && m)) {
            break;
        }
        solve(n, m);
    }
    system("pause");
}

```
