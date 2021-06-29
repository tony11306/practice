```c++
#include<bits/stdc++.h>
#define ll long long
#define endl "\n"
#define dbg1(x) cout<<"Dbg--> "<<'['<<#x<<':'<<x<<']'<<endl
#define dbg2(x,y) cout<<"Dbg--> "<<'['<<#x<<':'<<x<<' '<<#y<<':'<<y<<']'<<endl
#define dbg3(x,y,z) cout<<"Dbg--> "<<'['<<#x<<':'<<x<<' '<<#y<<':'<<y<<' '<<#z<<':'<<z<<']'<<endl
#define iss std::ios::sync_with_stdio(0);std::cin.tie(0)
using namespace std; 


bool isOutside(pair<int, int> pos, int rows, int cols) {
   if(pos.first < 0 || pos.first >= rows) {
      return true;
   }

   if(pos.second < 0 || pos.second >= cols) {
      return true;
   }

   return false;
}

void solve(int rows, int cols, int entry) {
   char g[rows][cols];
   int steps[rows][cols];
   for(int i = 0; i < rows; ++i) {
      for(int j = 0; j < cols; ++j) {
         cin >> g[i][j];
         steps[i][j] = 0;
      }
   }

   pair<int, int> current = {0, entry-1};
   steps[0][entry-1] = 1;

   while(true) {
      pair<int, int> prev = {current.first, current.second};
      if(g[current.first][current.second] == 'N') {
         current.first--;
      } else if(g[current.first][current.second] == 'S') {
         current.first++;
      } else if(g[current.first][current.second] == 'W') {
         current.second--;
      } else if(g[current.first][current.second] == 'E') {
         current.second++;
      }

      if(isOutside(current, rows, cols)) {
         cout << steps[prev.first][prev.second] << " step(s) to exit" << endl; 
         return;
      } else if(steps[current.first][current.second] != 0) {
         cout << steps[current.first][current.second]-1 << " step(s) before a loop of " << steps[prev.first][prev.second] - (steps[current.first][current.second]-1) << " step(s)" << endl;
         return;
      } else {
         steps[current.first][current.second] = steps[prev.first][prev.second] + 1;
      }

   }
   


}

int main() {
   int rows;
   int cols;
   int entry;
   while(cin >> rows >> cols >> entry) {
      if(rows == 0 && cols == 0 && entry == 0) {
         break;
      }
      solve(rows, cols, entry);
   }
   system("pause");
}
```
