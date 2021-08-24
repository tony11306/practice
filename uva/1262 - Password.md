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
    set<char> grid1[5];
    set<char> grid2[5];
    int n;
    cin >> n;
    char c;
    for(int i = 0; i < 6; ++i) {
        for(int j = 0; j < 5; ++j) {
            cin >> c;
            grid1[j].insert(c);
        }
    }
    for(int i = 0; i < 6; ++i) {
        for(int j = 0; j < 5; ++j) {
            cin >> c;
            grid2[j].insert(c);
        }
    }

    vector<string> st1;
    vector<string> st2;

    for(char c1: grid1[0]) {
        for(char c2: grid1[1]) {
            for(char c3: grid1[2]) {
                for(char c4: grid1[3]) {
                    for(char c5: grid1[4]) {    
                        string s = "";
                        s += c1;
                        s += c2;
                        s += c3;
                        s += c4;
                        s += c5;
                        //cout << s << endl;
                        st1.push_back(s);
                    }
                }
            }
        }
    }

    vector<string> ans;

    for(char c1: grid2[0]) {
        for(char c2: grid2[1]) {
            for(char c3: grid2[2]) {
                for(char c4: grid2[3]) {
                    for(char c5: grid2[4]) {    
                        string s = "";
                        s += c1;
                        s += c2;
                        s += c3;
                        s += c4;
                        s += c5;
                        st2.push_back(s);
                    }
                }
            }
        }
    }
    set_intersection(ALL(st1), ALL(st2), back_inserter(ans));
    if(n > ans.size()) {
        cout << "NO" << endl;
    } else {
        cout << ans[n-1] << endl;
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
