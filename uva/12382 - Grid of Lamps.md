```c++
#include<bits/stdc++.h>
#define ll long long
#define endl "\n"
#define dbg1(x) cout<<"Dbg--> "<<'['<<#x<<':'<<x<<']'<<endl
#define dbg2(x,y) cout<<"Dbg--> "<<'['<<#x<<':'<<x<<' '<<#y<<':'<<y<<']'<<endl
#define dbg3(x,y,z) cout<<"Dbg--> "<<'['<<#x<<':'<<x<<' '<<#y<<':'<<y<<' '<<#z<<':'<<z<<']'<<endl
#define ALL(x) x.begin(), x.end()
#define FOR_EACH_CASE(x) for(int cas = 1; cas <= x && (cout << "Case #" << cas << ": "); ++cas)
#define iss std::ios::sync_with_stdio(0);std::cin.tie(0)
using namespace std;
const int INF = ~(1<<31);
const int INF_0x3f = 0x3f3f3f3f;

void solve() {
    int rows;
    int cols;
    cin >> rows >> cols;
    vector<int> rowsV(rows);
    vector<int> colsV(cols);
    for(int i = 0; i < rows; ++i) {
        cin >> rowsV[i];
    }
    for(int j = 0; j < cols; ++j) {
        cin >> colsV[j];
    }

    int rowP = 0;
    int colP = 0;
    int ans = 0;
    sort(ALL(rowsV), greater<int>());
    sort(ALL(colsV), greater<int>());
    
    for(int i = 0; i < rows; ++i) {
        for(int j = 0; j < cols && rowsV[i] > 0; ++j) {
            if(rowsV[i] && colsV[j]) {
                ans++;
                rowsV[i]--;
                colsV[j]--;
            }
        }
        ans += rowsV[i];
        sort(ALL(colsV), greater<int>());
    }

    for(int j = 0; j < cols; ++j) {
        ans += colsV[j];
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
