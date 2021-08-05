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

void solve(int n) {
    int a;
    while(cin >> a && a != 0) {
        vector<int> goal;
        goal.push_back(a);
        for(int i = 1; i < n; ++i) {
            cin >> a;
            goal.push_back(a);
        }

        stack<int> station;
        stack<int> dirA;
        stack<int> dirB;
        for(int i = 0; i < n; ++i) {
            dirA.push(n-i);
        }
        bool ans = true;
        while(!dirA.empty() || !station.empty()) {
            if(!dirA.empty() && dirA.top() == goal[dirB.size()]) {
                dirB.push(dirA.top());
                dirA.pop();
            } else if(!station.empty() && station.top() == goal[dirB.size()]) {
                dirB.push(station.top());
                station.pop();
            } else if(!dirA.empty()) {
                station.push(dirA.top());
                dirA.pop();
            } else {
                ans = false;
                break;
            }
        }

        if(ans) {
            cout << "Yes" << endl;
        } else {
            cout << "No" << endl;
        }
        

    }

}

int main() {
    int n;
    while(cin >> n && n != 0) {
        solve(n);
        cout << endl;
    }
    system("pause");
}

```
