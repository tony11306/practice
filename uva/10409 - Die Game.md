```c++
// 這麼水的嗎
#include<bits/stdc++.h>
#define ll long long
#define endl "\n"
#define dbg1(x) cout<<"Dbg--> "<<'['<<#x<<':'<<x<<']'<<endl
#define dbg2(x,y) cout<<"Dbg--> "<<'['<<#x<<':'<<x<<' '<<#y<<':'<<y<<']'<<endl
#define dbg3(x,y,z) cout<<"Dbg--> "<<'['<<#x<<':'<<x<<' '<<#y<<':'<<y<<' '<<#z<<':'<<z<<']'<<endl
#define ALL(x) x.begin(), x.end()
#define FOR_EACH_CASE(x) for(int cas = 1; cas <= x && (cout << "Case " << cas << ": "); ++cas)
#define iss std::ios::sync_with_stdio(0);std::cin.tie(0)
using namespace std;
const int INF = ~(1<<31);
const int INF_0x3f = 0x3f3f3f3f;

void solve(int n) {
    int top = 1;
    int north = 2;
    int west = 3;
    while(n--) {
        string command;
        cin >> command;
        if(command == "north") {
            int tmp = top;
            top = 7 - north;
            north = tmp;
        } else if(command == "south") {
            int tmp = top;
            top = north;
            north = 7 - tmp;
        } else if(command == "west") {
            int tmp = top;
            top = 7 - west;
            west = tmp;
        } else {
            int tmp = top;
            top = west;
            west = 7 - tmp;
        }

    }
    cout << top << endl;

}

int main() {
    int n;
    while(cin >> n && n != 0) {
        solve(n);
    }
    system("pause");
}

```
