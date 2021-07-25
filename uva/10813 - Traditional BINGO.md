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

bool isRightDiagonal(int n, int m) {
    return n == m;
}

bool isLeftDiagonal(int n, int m) {
    return n + m + 1 == 5;
}

void solve() {
    pair<int, int> arr[76];
    for(int i = 0; i < 5; ++i) {
        for(int j = 0; j < 5; ++j) {
            if(i == 2 && j == 2) {
                continue;
            }
            int n;
            cin >> n;
            arr[n].first = i+1;
            arr[n].second = j+1;
        }
    }
    int row[5] = {0};
    int col[5] = {0};
    int leftDiagonal = 0;
    int rightDiagonal = 0;
    bool isFound = false;
    int m = 75;
    int n;
    int cnt = 0;
    while(m--) {
        cnt++;
        cin >> n;
        if(isFound) {
            continue;
        }

        if(leftDiagonal == 4 || rightDiagonal == 4 || row[2] == 4 || col[2] == 4) {
            cout << "BINGO after " << cnt-1 << " numbers announced" << endl;
            isFound = true;
            continue;
        }

        if(arr[n].first == 0 && arr[n].second == 0) {
            continue;
        }

        row[arr[n].first-1]++;
        col[arr[n].second-1]++;
        if(isLeftDiagonal(arr[n].first-1, arr[n].second-1)) {
            leftDiagonal++;
        }
        if(isRightDiagonal(arr[n].first-1, arr[n].second-1)) {
            rightDiagonal++;
        }
        
        for(int i = 0; i < 5; ++i) {
            isFound = isFound || row[i] == 5 || col[i] == 5;
        }

        if(isFound) {
            cout << "BINGO after " << cnt << " numbers announced" << endl;
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
