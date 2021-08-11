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

map<string, string> mp;
int n, m;
int main() {
    cin >> n >> m;
    while(n--) {
        string key, val;
        cin >> key >> val;
        mp[key] = val;
    }
    string key;
    while(m--) {
        cin >> key;
        string end2;
        char c = key[key.size()-2];
        if(key.size() >= 2) {
            end2 = key.substr(key.size()-2, 2);
        }
        if(mp.find(key) != mp.end()) {
            cout << mp[key] << endl;
        } else if(key.back() == 'y' && (c != 'a' && c != 'e' && c != 'i' && c != 'o' && c != 'u')) {
            cout << key.substr(0, key.size()-1) + "ies" << endl;
        } else if(key.back() == 'o' || key.back() == 's' || key.back() == 'x') {
            cout << key + "es" << endl;
        } else if(key.size() >= 2 && (end2 == "ch" || end2 == "sh")) {
            cout << key + "es" << endl;
        } else {
            cout << key + 's' << endl;
        }
    }

    system("pause");
}
```
