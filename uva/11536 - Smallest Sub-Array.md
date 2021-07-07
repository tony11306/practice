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
  
   int n;
   int m;
   int k;
   cin >> n >> m >> k;
   vector<int> arr(n);
   set<int> st;
   int cnts[k] = {0}; // 數第 i 個數字出現的次數
   int ans = n;
   int l = 0, r = 0;
   for(int i = 0; i < n; ++i) {
      if(i < 3) {
         arr[i] = i+1;
      } else {
         arr[i] = (arr[i-3] + arr[i-2] + arr[i-1]) % m + 1;
      }

      if(arr[i] >= 1 && arr[i] <= k) {
         if(st.size() != k) { // 先判斷第一次完整出現 1~k 的子陣列
            cnts[arr[i]-1]++;
            r = i;
         }
         st.insert(arr[i]);
      }
   }
   
   if(st.size() != k) { // 若大小不符合 k 代表有缺數字
      cout << "sequence nai" << endl;
      return;
   }

   if(cnts[arr[l]-1] > 1) { 
      // 這一段很醜，由於 l 預設從 0 開始
      // 但是以 {1 2 3 7 1 12 9 11 9 6 3 7 5 4 5 3 1 10 3 3}, k = 4 為例
      // 左側應該要內縮，因為 1 出現的次數 > 1
      // 所以做完後 l = 1, r = 13
      while(true) {
         if(arr[l] >= 1 && arr[l] <= k) {
            if(cnts[arr[l]-1] == 1) {
               break;
            } else {
               cnts[arr[l]-1]--;
            }
         }
         l++;
      }
   }

   ans = r - l + 1;
   r++; // r += 1 是因為 r 已經判斷過了，所以要先 +1
   while(r < n) {
      if(arr[r] >= 1 && arr[r] <= k) {
         cnts[arr[r]-1]++;
      }

      if(cnts[arr[l]-1] > 1) { // 跟上面那段一模一樣，所以才說很醜
         while(true) {
            if(arr[l] >= 1 && arr[l] <= k) {
               if(cnts[arr[l]-1] == 1) {
                  break;
               } else {
                  cnts[arr[l]-1]--;
               }
            }
            
            l++;
         }
      }
      ans = min(ans, r-l+1); // 做完後每次取最小
      r++;

   }

   cout << ans << endl;


}

int main() {
   int n;
   cin >> n;
   FOR_EACH_CASE(n) {
      solve();
   }
   system("pause");
}
```
