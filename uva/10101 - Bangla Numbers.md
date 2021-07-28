```c++
// 我先說這種要搞空白格式輸出的都是狗屎..
// 操 害我看到快中風
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

string convert(ll n) {
    string ans = "";
    int kuti = n / 10000000;    
    if(kuti != 0) {
        if(kuti >= 100) {
            ans += convert(kuti) + "kuti ";
        } else {
            ans += to_string(kuti) + " kuti ";
        }
        
    }
    n %= 10000000;
    int lakh = n / 100000;
    if(lakh != 0) {
        ans += to_string(lakh) + " lakh ";
    }
    n %= 100000;
    int hajar = n / 1000;
    if(hajar != 0) {
        ans += to_string(hajar) + " hajar ";
    }
    n %= 1000;
    int shata = n / 100;
    if(shata != 0) {
        ans += to_string(shata) + " shata ";
    }
    n %= 100;
    if(n != 0) {
        ans += to_string(n) + " ";
    }
    return ans;
}

void solve(ll n) {
    if(n == 0) {
        cout << 0 << endl;
        return;
    }
    string ans = "";
    ans = convert(n);
    cout << ans.substr(0, ans.length()-1) << endl;
}

int main() {
    int cas = 1;
    ll n;
    while(cin >> n && cout << setw(4) << cas++ << ". ") {
        solve(n);
    }
    system("pause");
}

```
