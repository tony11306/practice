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


void solve(int n, int m) {
    vector<int> res;

    while(n) {
        if(m == 1 || m == 0 || n != 1 && n % m != 0) {
            cout << "Boring!" << endl;
            return;
        }
        res.push_back(n);
        n /= m;
    }
    if(res.size() <= 1) {
        cout << "Boring!" << endl;
        return;
    }
    for(int i = 0; i < res.size(); ++i) {
        cout << res[i];
        if(i != res.size() - 1) cout << " ";
    }
    
    cout << endl;
}

int main() {
    int n, m;
    while(cin >> n >> m) {
        solve(n, m);
    }
    system("pause");
}
```
