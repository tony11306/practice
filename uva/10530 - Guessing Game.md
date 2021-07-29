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



int main() {
    
    int n;
    int _max = 11, _min = 0;
    int flag = true;
    while(cin >> n) {
        cin.get();
        if(n == 0) {
            break;
        }
        string s;
        getline(cin, s);
        if(s == "right on") {
            if(_max > n && _min < n) {
                cout << "Stan may be honest" << endl;
            } else {
                cout << "Stan is dishonest" << endl;
            }
            _max = 11;
            _min = 0;
            continue;
        }
        if(s == "too low") {
            _min = max(n, _min);
        } else if(s == "too high" && n != 11) {
            _max = min(n, _max);
        }

    }
    system("pause");
}

```
