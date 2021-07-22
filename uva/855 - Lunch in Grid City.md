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
    int n, m;
    int t;
    cin >> n >> m >> t;
    vector<int> arr1;
    vector<int> arr2;
    while(t--) {
        int s, a;
        cin >> s >> a;
        arr1.push_back(s);
        arr2.push_back(a);
    }
    sort(arr1.begin(), arr1.end());
    sort(arr2.begin(), arr2.end());
    cout << "(Street: " << arr1[(arr1.size()-1)/2] << ", Avenue: " << arr2[(arr2.size()-1)/2] << ")" << endl;
    
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
