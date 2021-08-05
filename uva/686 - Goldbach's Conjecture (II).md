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

bool isPrime[32769];
vector<int> primes;
void buildPrime() {
    memset(isPrime, true, sizeof(isPrime));
    isPrime[0] = false;
    isPrime[1] = false;
    for(int i = 2; i < 32769; ++i) {
        if(isPrime[i]) {
            primes.push_back(i);
            for(int j = 2; i*j < 32769; ++j) {
                isPrime[i*j] = false;
            }
        }
    }
}

void solve(int n) {
    bool isUsed[32769] = {false};
    int ans = 0;
    for(int prime : primes) {
        if(prime > n/2) {
            break;
        }
        if(isPrime[n-prime] && !isUsed[prime] && !isUsed[n-prime]) {
            isUsed[prime] = true;
            isUsed[n-prime] = true;
            ans++;
        }
    }
    cout << ans << endl;

}

int main() {
    int n;
    buildPrime();
    while(cin >> n && n != 0) {
        solve(n);
    }
    system("pause");
}

```
