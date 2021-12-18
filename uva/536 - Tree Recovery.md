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

void solve(string preorder, string inorder) {
    if(preorder.length() == 0) {
        return;
    }
    if(preorder.length() == 1) {
        cout << preorder;
        return;
    }
    char mid = preorder[0];
    int l;
    for(int i = 0; i < inorder.length(); ++i) {
        if(mid == inorder[i]) {
            l = i;
            break;
        }
    }
    solve(preorder.substr(1, l), inorder.substr(0, l));
    solve(preorder.substr(l+1, preorder.length() - (l+1)), inorder.substr(l+1, inorder.length() - (l+1)));
    cout << mid;

}

int main() {
    string s1, s2;
    while(cin >> s1 >> s2) {
        solve(s1, s2);
        cout << endl;
    }
    system("pause");
}
```
