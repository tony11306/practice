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

void solve() {
    int n;
    set<vector<int>> st;
    cin >> n;
    vector<int> arr(n);
    for(int i = 0; i < n; ++i) {
        cin >> arr[i];
    }
    st.insert(arr);
    while(true) {
        int begin = arr[0];
        bool isAllZero = true;
        for(int i = 0; i < n-1; ++i) {
            arr[i] = abs(arr[i+1] - arr[i]);
            isAllZero = isAllZero && arr[i] == 0;
        }
        arr[n-1] = abs(begin - arr[n-1]);
        isAllZero = isAllZero && arr[n-1] == 0;
        int siz = st.size();
        st.insert(arr);
        if(isAllZero) {
            cout << "ZERO" << endl;
            return;
        } else if(siz == st.size()) {
            cout << "LOOP" << endl;
            return;
        }
    }
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
