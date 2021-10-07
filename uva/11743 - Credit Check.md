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

void solve() {
    string s;
    getline(cin, s);
    stringstream ss(s);
    string card = "";
    string tmp;
    while(ss >> tmp) {
        card += tmp;
    }
    int a = 0;
    int b = 0;
    for(int i = 0; i < card.length(); ++i) {
        if(i % 2 == 0) {
            tmp = to_string((card[i] - '0')*2);
            for(char c : tmp) {
                a += (c - '0');
            }
        } else {
            b += (card[i] - '0');
        }
    }

    string ans = to_string(a+b);
    if(ans[ans.length()-1] == '0') {
        cout << "Valid" << endl;
    } else {
        cout << "Invalid" << endl;
    }



}

int main() {
    int n;
    cin >> n;
    cin.get();
    while(n--) {
        solve();
    }
    system("pause");
}

```
