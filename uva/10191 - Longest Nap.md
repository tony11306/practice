```c++
// 總共就480分鐘 開陣列 暴力區間更新
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


void solve(int n) {
    string s;
    pair<int, int> ans;
    vector<bool> arr(481, 0);

    while(n--) {
        getline(cin, s);
        stringstream ss(s);
        string start;
        string end;
        ss >> start >> end;
        int st;
        int en;
        st = stoi(start.substr(0, 2))*60 + stoi(start.substr(3, 2)) - 600;
        en = stoi(end.substr(0, 2))*60 + stoi(end.substr(3, 2)) - 600;
        for(int i = st; i < en; ++i) {
            arr[i] = true;
        }
    }
    bool flag = false;
    int tmpStart = 0;
    int tmp = 0;
    for(int i = 0; i < 481; ++i) {
        
        if(flag && !arr[i]) {
            tmpStart = i;
            tmp = 1;
            flag = false;
            continue;
        }

        if(!arr[i]) {
            tmp++;
        } else {
            flag = true;
            if(tmp > ans.first) {
                ans.first = tmp;
                ans.second = tmpStart;
            }
        }
        if(i == 480) {
            tmp--;
            if(tmp > ans.first) {
                ans.first = tmp;
                ans.second = tmpStart;
            }
        }
    }

    ans.second += 600;
    if(ans.first < 60) {
        cout << "the longest nap starts at " << ans.second / 60 << ":" << setw(2) << setfill('0') << ans.second % 60; 
        cout << " and will last for " << ans.first << " minutes." << endl;
    } else {
        cout << "the longest nap starts at " << ans.second / 60 << ":" << setw(2) << setfill('0') << ans.second % 60; 
        cout << " and will last for " << ans.first / 60 << " hours and " << ans.first % 60 << " minutes." << endl;
    }

}

int main() {
    int n;
    int cas = 1;
    while(cin >> n && cout << "Day #" << cas++ << ": ") {
        cin.get();
        solve(n);
    }
    system("pause");
}
```
