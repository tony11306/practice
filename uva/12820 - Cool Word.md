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


void solve(int n) {
   int ans = 0;
   while(n--) {
      map<char, int> mp;
      set<int> st;
      string s;
      cin >> s;
      for(char c : s) {
         mp[c]++;
      }

      if(mp.size() < 2) {
         continue;
      }

      for(auto pr : mp) {
         st.insert(pr.second);
      }

      if(st.size() != mp.size()) {
         continue;
      }

      ans++;

   }

   cout << ans << endl;
}

int main() {
   int n;
   int cas = 1;
   while(cin >> n) {
      cout << "Case " << cas << ": ";
      solve(n);
      cas++;
   }
   system("pause");
}
```
