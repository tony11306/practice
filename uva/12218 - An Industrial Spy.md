```c++
#include<bits/stdc++.h>
#define ll long long
#define endl "\n"
#define dbg1(x) cout<<"Dbg--> "<<'['<<#x<<':'<<x<<']'<<endl
#define dbg2(x,y) cout<<"Dbg--> "<<'['<<#x<<':'<<x<<' '<<#y<<':'<<y<<']'<<endl
#define dbg3(x,y,z) cout<<"Dbg--> "<<'['<<#x<<':'<<x<<' '<<#y<<':'<<y<<' '<<#z<<':'<<z<<']'<<endl
#define iss std::ios::sync_with_stdio(0);std::cin.tie(0)
using namespace std; 


bool isPrimes[10000001];
set<int> ans;
void buildPrimes() {
   memset(isPrimes, 1, sizeof(isPrimes));
   isPrimes[0] = false;
   isPrimes[1] = false;
   for(int i = 2; i < 10000000; ++i) {

      if(!isPrimes[i]) {
         continue;
      }

      for(int j = 2; j*i < 10000000; ++j) {
         isPrimes[i*j] = false;
      }

   }
   
}

void solve(string s) {
   //cout << s << endl;
   for(int i = 0; i < s.length() && s.length() > 1; ++i) {
      solve(s.substr(0, i) + s.substr(i+1, s.length()-i-1));
   }

   do {
      if(isPrimes[stoi(s)]) {
         ans.insert(stoi(s));
      }
   } while(next_permutation(s.begin(), s.end()));

}

int main() {
   buildPrimes();
   int n;
   cin >> n;
   while(n--) {
      ans.clear();
      string s;
      cin >> s;
      sort(s.begin(), s.end());
      solve(s);
      cout << ans.size() << endl;
   }
   system("pause");
}
```
