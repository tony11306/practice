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

void solve(int n) {
    map<int, vector<int>> mp;
    while(n--) {
        int p, d;
        cin >> p >> d;
        mp[d].push_back(p);
    }

    priority_queue<int, vector<int>, greater<int>> arr;
    for(auto it = mp.begin(); it != mp.end(); it++) {
        for(auto p : it->second) {
            if(arr.size() < it->first) {
                arr.push(p);
            } else if(arr.top() < p) {
                arr.pop();
                arr.push(p);
            }
        }
        
    }
    ll ans = 0;
    while(!arr.empty()) {
        ans += arr.top();
        arr.pop();
    }

    cout << ans << endl;
    
}

int main() {
    int n;
    while(cin >> n) {
        solve(n);
    }
    system("pause");
}
```
