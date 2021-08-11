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

ll squareDigit(string s) {
    ll ans = 0;
    for(char c : s) {
        ans += (c-'0') * (c-'0');
    }
    return ans;
}

void solve() {
    string s;
    cin >> s;
    string t = s;
    bool isHappy = true;
    set<ll> st;
    while(true) {
        ll sd = squareDigit(t);
        if(st.find(sd) != st.end()) {
            isHappy = false;
            break;
        } else if(sd == 1) {
            break;
        }
        t = to_string(sd);
        st.insert(sd);
    }
    if(isHappy) {
        cout << s << " is a Happy number." << endl;
    } else {
        cout << s << " is an Unhappy number." << endl;
    }
}

int main() {
    int n;
    cin >> n;
    FOR_EACH_CASE(n) {
        solve();
    }
    system("pause");
}
```
