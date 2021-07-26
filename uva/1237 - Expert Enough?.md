```c++
// 感覺排序搜尋就好...
// 我以為是區間修改 單點查詢問題
// 直接砸了 bit + 差分陣列
// 最後想不到怎麼查覆蓋到的顏色 直接暴搜
// 總感覺我的寫法越來越毒瘤 ==
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

int lowbit(int x) {
    return x & -x;
}

void update(vector<int>& bit, int n, int d) {
    while(n < 1000001) {
        bit[n] += d;
        n += lowbit(n);
    }
}

int query(vector<int>& bit, int n) {
    int ans = 0;
    while(n >= 1) {
        ans += bit[n];
        n -= lowbit(n);
    }
    return ans;
}

void solve() {
    vector<int> bit(1000001);
    int n;
    cin >> n;
    map<pair<int, int>, string> mp;
    while(n--) {
        string s;
        int l, r;
        cin >> s >> l >> r;
        mp[make_pair(l, r)] = s;
        update(bit, l, 1);
        update(bit, r+1, -1);
    }
    cin >> n;
    while(n--) {
        int a;
        cin >> a;
        int sum = query(bit, a);
        if(sum == 1) {
            for(auto it = mp.begin(); it != mp.end(); ++it) {
                if(it->first.first <= a && it->first.second >= a) {
                    cout << it->second << endl;
                    break;
                }
            }
        } else {
            cout << "UNDETERMINED" << endl;
        }
    }
}

int main() {
    int n;
    cin >> n;
    n--;
    solve();
    while(n--) {
        cout << endl;
        solve();
    }
    system("pause");
}

```
