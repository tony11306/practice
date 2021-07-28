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

int clockwiseDistance(int a, int b) { // a to b
    if(a > b) {
        return a-b;
    }
    return 40-b+a;
}

int counterClockwiseDistance(int a, int b) { // a to b
    if(b > a) {
        return b-a;
    }
    return 40-a+b;
}

int main() {
    int a, b, c, d;
    while(cin >> a >> b >> c >> d) {
        if(a == 0 && b == 0 && c == 0 && d == 0) {
            break;
        }
        cout << (120+clockwiseDistance(a, b)+counterClockwiseDistance(b, c)+clockwiseDistance(c, d))*9 << endl;
    }
    system("pause");
}
// 40 + 40 + 30
```
