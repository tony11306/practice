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


void solve() {
   int n, m;
   cin >> n >> m;
   char g[n][m];
   map<char, set<pair<int, int>>> mp;
   for(int i = 0; i < n; ++i) {
      for(int j = 0; j < m; ++j) {
         cin >> g[i][j];
         g[i][j] = tolower(g[i][j]);
         mp[g[i][j]].insert(make_pair(i, j));
      }
   }

   int k;
   cin >> k;
   string s;
   while(k--) {
      cin >> s;
      pair<int, int> ans;

      for(int i = 0; i < s.length(); ++i) {
         s[i] = tolower(s[i]);
      }

      for(pair<int, int> pr : mp[tolower(s[0])]) {
         string s2 = "";
         for(int i = 0; i < s.length() && pr.first-s.length()+1 >= 0; ++i) { // 上
            s2 += g[pr.first-i][pr.second];
         }
         if(s2 == s) {
            ans = pr;
            break;
         } else {
            s2 = "";
         }

         for(int i = 0; i < s.length() && pr.first+s.length() <= n; ++i) { // 下
            s2 += g[pr.first+i][pr.second];
         }

         if(s2 == s) {
            ans = pr;
            break;
         } else {
            s2 = "";
         }

         for(int i = 0; i < s.length() && pr.second-s.length()+1 >= 0; ++i) { // 左
            s2 += g[pr.first][pr.second-i];
         }

         if(s2 == s) {
            ans = pr;
            break;
         } else {
            s2 = "";
         }

         for(int i = 0; i < s.length() && pr.second+s.length() <= m; ++i) { // 右
            s2 += g[pr.first][pr.second+i];
         }

         if(s2 == s) {
            ans = pr;
            break;
         } else {
            s2 = "";
         }
         
         for(int i = 0; i < s.length() && pr.second-s.length()+1 >= 0 && pr.first-s.length()+1 >= 0; ++i) { // 左上
            s2 += g[pr.first-i][pr.second-i];
         }

         if(s2 == s) {
            ans = pr;
            break;
         } else {
            s2 = "";
         }

         for(int i = 0; i < s.length() && pr.second-s.length()+1 >= 0 && pr.first+s.length() <= n; ++i) { // 左下
            s2 += g[pr.first+i][pr.second-i];
         }

         if(s2 == s) {
            ans = pr;
            break;
         } else {
            s2 = "";
         }

         for(int i = 0; i < s.length() && pr.second+s.length() <= m && pr.first-s.length()+1 >= 0; ++i) { // 右上
            s2 += g[pr.first-i][pr.second+i];
         }

         if(s2 == s) {
            ans = pr;
            break;
         } else {
            s2 = "";
         }

         for(int i = 0; i < s.length() && pr.second+s.length() <= m && pr.first+s.length() <= n; ++i) { // 右下
            s2 += g[pr.first+i][pr.second+i];
         }

         if(s2 == s) {
            ans = pr;
            break;
         } else {
            s2 = "";
         }

      }

      cout << ans.first+1 << " " << ans.second+1 << endl;
      
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
