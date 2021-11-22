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

map<char, int> priority = {
    {'+', 0},
    {'-', 0},
    {'*', 1},
    {'/', 1},
    {'(', -1}
};

void solve(string s) {
    stack<char> sta;
    string ans = "";

    for(char c : s) {
        if(isdigit(c)) {
            ans += c;
        } else if(c == '(') {
            sta.push(c);
        } else if(c == ')') {
            while(!sta.empty() && sta.top() != '(') {
                ans += sta.top();
                sta.pop();
            }
            if(!sta.empty()) {
                sta.pop();
            }
        } else if(sta.empty()) {
            sta.push(c);
        } else {
            while(!sta.empty() && priority[c] <= priority[sta.top()]) {
                ans += sta.top();
                sta.pop();
            }
            sta.push(c);
        }
    }
    while(!sta.empty()) {
        ans += sta.top();
        sta.pop();
    }
    cout << ans << endl;
}

int main() {
    int n;
    cin >> n;
    cin.get();
    string s;
    bool isFirst = true;
    getline(cin, s);
    while(n--) {
        string eq = "";
        while(getline(cin, s)) {
            if(s == "") {
                break;
            } else {
                eq += s[0];
            }
        }

        if(isFirst) {
            solve(eq);
            isFirst = false;
        } else {
            cout << endl;
            solve(eq);
        }
    }
    system("pause");
}
```
