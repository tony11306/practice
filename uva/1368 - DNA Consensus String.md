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
    int n;
    int l;
    cin >> n >> l;
    int arr[l][4]; // A T C G
    memset(arr, 0, sizeof(arr));
    while(n--) {
        string s;
        cin >> s;
        for(int i = 0; i < s.length(); ++i) {
            if(s[i] == 'A') {
                arr[i][0]++;
            } else if(s[i] == 'T') {
                arr[i][1]++;
            } else if(s[i] == 'C') {
                arr[i][2]++;
            } else if(s[i] == 'G') {
                arr[i][3]++;
            }
        }
    }

    int err = 0;
    string s = "";
    for(int i = 0; i < l; ++i) {
        int maxCnt = *max_element(arr[i], arr[i]+4);
        err += arr[i][0] + arr[i][1] + arr[i][2] + arr[i][3] - maxCnt;
        if(maxCnt == arr[i][0]) {
            s += 'A';
        } else if(maxCnt == arr[i][2]) {
            s += 'C';
        } else if(maxCnt == arr[i][3]) {
            s += 'G';
        } else if(maxCnt == arr[i][1]) {
            s += 'T';
        }
    }

    cout << s << endl << err << endl;
    
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
