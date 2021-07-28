```c++
// 純粹建表查表
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

int table[100001];

int generator(int a) {
    int b = a;
    while(a) {
        b += a % 10;
        a /= 10;
    }
    return b;

}

void buildTable() {
    memset(table, 0x3f, sizeof(table));
    for(int i = 1; i <= 100000; ++i) {
        int gen = generator(i);
        if(gen <= 100000) {
            table[gen] = min(table[gen], i);
        }
    }
}

int main() {
    buildTable();
    int n;
    cin >> n;
    while(n--) {
        int q;
        cin >> q;
        if(table[q] != INF_0x3f) {
            cout << table[q] << endl;
        } else {
            cout << 0 << endl;
        }
    }
    system("pause");
}

```
