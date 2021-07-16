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

void solve() {
    string s;
    cin >> s;
    int arr[s.size()] = {0};
    int ans = 0;
    arr[0] = s[0] == 'O' ? 1 : 0;
    ans = arr[0];
    for(int i = 1; i < s.size(); ++i) {
        if(s[i] == 'O') {
            arr[i] = arr[i-1] + 1;
        } else {
            arr[i] = 0;
        }
        ans += arr[i];
    }
    cout << ans << endl;

}

int main() {
    int n;
    cin >> n;
    while(n--) {
        solve();
    }
    system("pause");
}
```
