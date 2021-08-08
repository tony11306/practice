```c++
// 找時間學看看矩陣快速冪好了
#include<bits/stdc++.h>
#define ll long long
#define endl "\n"
#define dbg1(x) cout<<"Dbg--> "<<'['<<#x<<':'<<x<<']'<<endl
#define dbg2(x,y) cout<<"Dbg--> "<<'['<<#x<<':'<<x<<' '<<#y<<':'<<y<<']'<<endl
#define dbg3(x,y,z) cout<<"Dbg--> "<<'['<<#x<<':'<<x<<' '<<#y<<':'<<y<<' '<<#z<<':'<<z<<']'<<endl
#define ALL(x) x.begin(), x.end()
#define FOR_EACH_CASE(x) for(int cas = 1; cas <= x && (cout << "Case " << cas << ": "); ++cas)
#define iss std::ios::sync_with_stdio(0);std::cin.tie(0)
using namespace std;
const int INF = ~(1<<31);
const int INF_0x3f = 0x3f3f3f3f;

string arr[5001];

string add(string s1, string s2) {
    if(s2.length() > s1.length()) {
        swap(s1, s2);
    }
    while(s1.length() != s2.length()) {
        s2 = "0" + s2;
    }
    reverse(ALL(s1));
    reverse(ALL(s2));

    int carry = 0;
    string ans = "";
    for(int i = 0; i < s1.length(); ++i) {
        ans += to_string((s1[i]-'0' + s2[i]-'0' + carry) % 10);
        carry = (s1[i]-'0' + s2[i]-'0' + carry) / 10;
    }
    if(carry > 0) {
        ans += to_string(carry);
    }
    reverse(ALL(ans));
    return ans;

}

int main() {
    arr[0] = "0";
    arr[1] = "1";
    for(int i = 2; i <= 5000; ++i) {
        arr[i] = add(arr[i-1], arr[i-2]);
    }
    int n;
    while(cin >> n) {
        cout << "The Fibonacci number for " << n << " is " << arr[n] << endl;
    }
    system("pause");
}
```
