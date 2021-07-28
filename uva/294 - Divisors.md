```c++
// 埃式篩建表
// 暴力質因數分解
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

vector<int> primes;

void buildPrimes() {
    bool isPrime[31623];
    memset(isPrime, true, sizeof(isPrime));
    isPrime[0] = false;
    isPrime[1] = false;
    for(int i = 2; i <= 31622; ++i) {
        if(isPrime[i]) {
            primes.push_back(i);
            for(int j = 2; i*j <= 31622; ++j) {
                isPrime[i*j] = false;
            } 
        }
        
    }
}

void solve() {
    int l, r;
    cin >> l >> r;
    if(l == 1 && r == 1) {
        cout << "Between 1 and 1, 1 has a maximum of 1 divisors." << endl;
        return;
    }
    int ans = l;
    int maxComb = 1;
    for(int val = l; val <= r; ++val) {
        int tmp = val;
        int comb = 1;
        for(int prime : primes) {
            int cnt = 0;
            while(tmp % prime == 0) {
                tmp /= prime;
                cnt++;
            }
            comb *= (cnt+1);
        }
        if(comb > maxComb) {
            maxComb = comb;
            ans = val;
        }
    }
    cout << "Between " << l << " and " << r << ", " << ans << " has a maximum of " << maxComb << " divisors." << endl;
}

int main() {
    buildPrimes();
    int n;
    cin >> n;
    while(n--) {
        solve();
    }

    system("pause");
}
```
