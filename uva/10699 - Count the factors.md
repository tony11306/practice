```c++
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

vector<int> table(1000001);

void buildTable() {
    vector<bool> isPrime(1000001, true);
    isPrime[1] = false;
    for(int i = 2; i < 1000001; ++i) {
        if(isPrime[i]) {
            table[i] = 1;
            for(int j = 2; i*j < 1000001; ++j) {
                isPrime[i*j] = false;
                table[i*j]++;
            }
        }
    }
}

int main() {
    buildTable();
    int n;
    while(cin >> n && n != 0) {
        cout << n << " : " << table[n] << endl;
    }
    system("pause");
}
```
