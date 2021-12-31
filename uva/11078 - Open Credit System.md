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

void solve() {
    int n;
    cin >> n;
    int arr[n];
    int minVal[n]; // 第 i 個元素起後最小的值
    for(int i = 0; i < n; ++i) {
        cin >> arr[i];
    }
    for(int i = n-1, currentMin = INF; i >= 0; --i) {
        if(arr[i] < currentMin) {
            minVal[i] = arr[i];
            currentMin = arr[i];
        } else {
            minVal[i] = currentMin;
        }
    }
    int ans = ~INF;
    for(int i = 0; i < n-1; ++i) {
        ans = max(ans, arr[i] - minVal[i+1]);
    }
    cout << ans << endl;
}

int main() {

    // 6 8 1 2 3 4 7 8 3
    int n;
    cin >> n;
    while(n--) {
        solve();
    }
    system("pause");
}
```
