```c++
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


#define y second
#define x first
int n, m; // n for x, m for y
set<pair<int, int>> lost;
const pair<int, int> direction[4] = {
    {0, 1},
    {1, 0},
    {0, -1},
    {-1, 0}
};

const char directionChar[4] = {'N', 'E', 'S', 'W'};

void solve() {
    pair<int, int> pos;
    int current;
    char start;
    string instructions;
    while(cin >> pos.x >> pos.y >> start >> instructions) {
        bool isLost = false;
        if(start == 'N') {
            current = 0;
        } else if(start == 'E') {
            current = 1;
        } else if(start == 'S') {
            current = 2;
        } else {
            current = 3;
        }
        for(char instruction : instructions) {
            pair<int, int> prev = pos;
            if(instruction == 'R') {
                current = (current + 1) % 4;
            } else if(instruction == 'L') {
                if(current == 0) {
                    current = 3;
                } else {
                    current = current - 1;
                }
            } else {
                pos.x += direction[current].x;
                pos.y += direction[current].y;
            }

            if(pos.x > n || pos.x < 0 || pos.y > m || pos.y < 0) {
                if(lost.find(prev) == lost.end()) {
                    isLost = true;
                    lost.insert(prev);
                    pos = prev;
                    break;
                } else {
                    pos = prev;
                }
                
            }

        }

        cout << pos.x << " " << pos.y << " " << directionChar[current];
        if(isLost) {
            cout << " LOST";
        }
        cout << endl;

    }
}

int main() {
    cin >> n >> m;
    solve();
    system("pause");
}
```
