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

void solve(int a, int b) {
    set<int> st1;
    set<int> st2;
    while(a--) {
        int c;
        cin >> c;
        st1.insert(c);
    }
    while(b--) {
        int c;
        cin >> c;
        st2.insert(c);
    }
    int ans1 = 0, ans2 = 0;
    for(int val : st1) {
        if(st2.find(val) == st2.end()) {
            ans1++;
        }
    }

    for(int val : st2) {
        if(st1.find(val) == st1.end()) {
            ans2++;
        }
    }
    cout << min(ans1, ans2) << endl;
}

int main() {
    int a, b;
    while(cin >> a >> b && a != 0 && b != 0) {
        solve(a, b);
    }
    system("pause");
}

```
