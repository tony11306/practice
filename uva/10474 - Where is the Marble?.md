```c++
// 排序二分搜 或 線搜
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

void solve(int n, int m) {
    vector<int> arr(n);
    for(int i = 0; i < n; ++i) {
        cin >> arr[i];
    }

    sort(arr.begin(), arr.end());

    while(m--) {
        int q;
        cin >> q;
        if(binary_search(arr.begin(), arr.end(), q)) {
            cout << q << " found at " << lower_bound(arr.begin(), arr.end(), q) - arr.begin() + 1 << endl;
        } else {
            cout << q << " not found" << endl;
        }
    }

}

int main() {
    int n, m;
    int cas = 1;
    while(cin >> n >> m) {
        if(n == 0 && m == 0) {
            break;
        }
        cout << "CASE# " << cas << ":" << endl;
        cas++;
        solve(n, m);
    }
    system("pause");
}
```
