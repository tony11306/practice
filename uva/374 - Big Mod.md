```c++
// 快速冪 + 餘數mod
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

int powAndMod(int b, int p, int m) {
    if(b == 0) {
        return 0;
    } else if(p == 0) {
        return 1;
    } else if(b == 1) {
        return b % m;
    }

    if(p%2 == 0) {
        int ans = powAndMod(b, p/2, m);
        return (ans * ans) % m;
    } else {
        int ans = powAndMod(b, (p-1)/2, m);
        return (((ans * ans) % m) * (b % m)) % m;
    }

}

int main() {
    int b, p, m;
    while(cin >> b >> p >> m) {
        cout << powAndMod(b, p, m) << endl;
    }
    system("pause");
}


```
