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

vector<int> primes;
bool isPrime[1001];
int dp[1001][1001];

void buildPrimes() {
    
    memset(isPrime, true, sizeof(isPrime));
    isPrime[0] = false;
    isPrime[1] = false;
    for(int i = 2; i <= 1000; ++i) {
        if(isPrime[i]) {
            primes.push_back(i);
            for(int j = 2; i*j <= 1000; ++j) {
                isPrime[i*j] = false;
            }
        }
    }
}

void buildDp() {
    memset(dp, 0x3f, sizeof(dp));
    for(int i = 1; i <= 1000; ++i) { // init
        dp[i][i] = 0;
        for(int prime : primes) {
            if(i+prime > 1000) {
                break;
            }
            if(i % prime == 0) {
                dp[i][i+prime] = 1;
            }
            
        }
        
    }

    for(int i = 1; i <= 1000; ++i) {
        for(int j = 1; j <= 1000; ++j) {
            if(i == j) {
                continue;
            } else if(isPrime[i] || isPrime[j]) {
                dp[i][j] = -1;
            } else if(i > j) {
                dp[i][j] = -1;
            } else if(i == 1) {
                dp[i][j] = -1;
            } else {
                for(int prime : primes) {
                    if(j-prime <= i) {
                        break;
                    }
                    if((j-prime) % prime == 0) {
                        if(dp[i][j-prime] != -1 && dp[i][j-prime] != INF_0x3f) {
                            dp[i][j] = min(dp[i][j-prime]+1, dp[i][j]);
                        }
                    } 
                    
                    
                }
            }
        }
    }

}

int main() {
    int s, t;
    buildPrimes();
    buildDp();

    FOR_EACH_CASE(INF && cin >> s >> t && s != 0 && t != 0) {
        cout << dp[s][t] << endl;
    }
    system("pause");
}
```
