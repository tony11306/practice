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



class Drug {
    public:
        string name;
        int freq;
        int priority;
        int cur;

        friend bool operator<(const Drug& a, const Drug& b) {
            if(a.cur == b.cur) {
                return a.priority < b.priority;
            }
            return a.cur < b.cur;
        }

        friend bool operator>(const Drug& a, const Drug& b) {
            return !(a < b);
        }
};

void solve() {
    int n, m;
    cin >> n >> m;
    priority_queue<Drug, vector<Drug>, greater<Drug>> pq;
    int maxT = 0;
    for(int i = 0; i < n; ++i) {
        Drug d;
        cin >> d.name >> d.freq;
        d.priority = i;
        d.cur = d.freq;
        pq.push(d);
    }

    while(m--) {
        Drug d = pq.top();
        cout << d.cur << " " << d.name << endl;
        pq.pop();
        d.cur += d.freq;
        pq.push(d);
    }


}

int main() {
    int n;
    cin >> n;
    while(n--) {
        solve();
    }
    system("pause");
}

```
