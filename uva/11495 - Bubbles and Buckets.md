```c++
// 用 bubble sort 估計會超時
// binary indexed tree 二元索引樹
// 或 mergeSort 求解
// 求逆序對數的題目

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

int lowbit(int a) {
    return a & (-a);
}

void add(int* bit, int n, int a) {
    while(a <= n) {
        bit[a]++;
        a += lowbit(a);
    }
}

int query(int* bit, int a) {
    int ans = 0;
    while(a >= 1) {
        ans += bit[a];
        a -= lowbit(a);
    }
    return ans;
}

void solve(int n) {
    int arr[n+1];
    int d[n+1]; // 第 i 大的數為 arr[d[i]]，用來離散化資料
    for(int i = 1; i <= n; ++i) {
        cin >> arr[i];
        d[i] = i;
    }
    sort(d+1, d+n+1, [&](int a, int b) {
        return arr[a] > arr[b];
    });
    int bit[n+1] = {0}; // binary indexed tree 1~n的已經存在的數
    int ans = 0;
    for(int i = 1; i <= n; ++i) {
        add(bit, n, d[i]);
        ans += query(bit, d[i]-1);
    }
    if(ans % 2 == 0) {
        cout << "Carlos" << endl;
    } else {
        cout << "Marcelo" << endl;
    }
    // cout << ans << endl; Cpe modified
}

int main() {
    int n;
    while(cin >> n && n != 0) {
        solve(n);
    }
    system("pause");
}
```
