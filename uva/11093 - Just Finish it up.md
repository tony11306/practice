
```cpp
#include<bits/stdc++.h>
#define ll long long
#define endl "\n"
#define dbg1(x) cout<<"Dbg--> "<<'['<<#x<<':'<<x<<']'<<endl
#define dbg2(x,y) cout<<"Dbg--> "<<'['<<#x<<':'<<x<<' '<<#y<<':'<<y<<']'<<endl
#define dbg3(x,y,z) cout<<"Dbg--> "<<'['<<#x<<':'<<x<<' '<<#y<<':'<<y<<' '<<#z<<':'<<z<<']'<<endl
#define iss std::ios::sync_with_stdio(0);std::cin.tie(0)
using namespace std; 

void solve() {
   int n;
   cin >> n;
   ll sum = 0;
   int arr[n];
   int arr2[n];
   int gap[n];
   for(int i = 0; i < n; ++i) {
      cin >> arr[i];
   }
   for(int i = 0; i < n; ++i) {
      cin >> arr2[i];
      gap[i] = arr[i] - arr2[i];
      sum += (arr[i] - arr2[i]);
   }

   if(sum < 0) {
      cout << "Not possible" << endl;
      return;
   }

   for(int i = 0; i < n; ++i) {
      int dest = (i == 0 ? n-1 : i-1);
      int current = i;
      int s = 0;
      bool isAns = true;
      while(current != dest) {
         s += gap[current];
         if(s < 0) {
            isAns = false;
            break;
         }
         current++;
         current %= n;
      }
      if(isAns) {
         cout << "Possible from station " << i+1 << endl;
         return;
      }
   }


}

int main() {
   int n;
   cin >> n;
   for(int i = 1; i <= n; ++i) {
      cout << "Case " << i << ": ";
      solve();
   }
   system("pause");
}
```
