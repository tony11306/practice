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


vector<int> primes;

void buildPrime() {
    bool isPrime[32768];
    memset(isPrime, true, sizeof(isPrime));
    isPrime[1] = false;

    for(int i = 2; i <= 32767; ++i) {
        if(isPrime[i]) {
            primes.push_back(i);
            for(int j = 2; i*j <= 32767; ++j) {
                isPrime[i*j] = false;
            }
        }
    }
    reverse(ALL(primes));
}

int myPow(int a, int b) {
    if(a == 1) {
        return 1;
    } else if(b == 0) {
        return 1;
    }

    int ans = 1;
    if(b % 2 == 0) {
        ans = myPow(a, b/2);
        ans *= ans;
    } else {
        ans = myPow(a, (b-1)/2);
        ans *= ans;
        ans *= a;
    }
    return ans;

}

void solve(string s) {
    stringstream ss(s);
    int n = 1;
    int a, b;
    while(ss >> a >> b) {
        n *= myPow(a, b);
    }

    n -= 1;
    bool flag = false;
    for(int prime : primes) {
        if(n % prime == 0) {
            int cnt = 0;
            while(n % prime == 0) {
                n /= prime;
                cnt++;
            }
            if(flag) {
                cout << " ";
            }
            cout << prime << " " << cnt;
            flag = true;

        }
        if(n == 1) {
            break;
        }
    }
    cout << endl;
    
}

int main() {
    string s;
    buildPrime();
    while(getline(cin, s) && s != "0") {
        solve(s);
    }
    system("pause");
}
```
