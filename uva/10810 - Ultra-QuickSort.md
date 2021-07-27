```c++
// 我一定要習慣bit
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

int lowbit(int n) {
    return n & -n;
}

void update(int* bit, int n, int a) {
    while(a <= n) {
        bit[a] += 1;
        a += lowbit(a);
    }
}

int query(int* bit, int n) {
    int ans = 0;
    while(n > 0) {
        ans += bit[n];
        n -= lowbit(n);
    }
    return ans;
}

void solve(int n) {
    int arr[n+1];
    int bit[n+1] = {0};
    int d[n+1];
    for(int i = 1; i <= n; ++i) {
        cin >> arr[i];
        d[i] = i;
    }

    sort(d+1, d+n+1, [&](int a, int b){
        return arr[a] >= arr[b];
    });
    ll ans = 0;
    for(int i = 1; i <= n; ++i) {
        update(bit, n, d[i]);
        ans += query(bit, d[i]-1);
    }

    cout << ans << endl;

}

int main() {
    int n;
    while(cin >> n && n != 0) {
        solve(n);
    }
    system("pause");
}

```
