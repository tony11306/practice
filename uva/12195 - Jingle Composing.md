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

void solve(string s) {
    
    s = s.substr(1, s.length()-1);
    map<char, int> mp = {
        {'W', 64},
        {'H', 32},
        {'Q', 16},
        {'E', 8},
        {'S', 4},
        {'T', 2},
        {'X', 1}
    };
    int cnt = 0;
    int ans = 0;
    for(char c : s) {
        if(c == '/') {
            if(cnt == 64) {
                ans++;
            }
            cnt = 0;
        } else {
            cnt += mp[c];
        }
    }

    cout << ans << endl;

}

int main() {
    string s;
    while(getline(cin, s)) {
        if(s == "*") {
            break;
        }
        solve(s);
    }
    system("pause");
}

```
