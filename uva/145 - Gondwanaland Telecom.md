```c++
// 輸出很g8 edge case 也很g8
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

double table[5][3] = {
    {0.10, 0.06, 0.02},
    {0.25, 0.15, 0.05},
    {0.53, 0.33, 0.13},
    {0.87, 0.47, 0.17},
    {1.44, 0.80, 0.30}
};

void solve(char cat) {
    string num;
    int startHour, startMin;
    int endHour, endMin;
    int day = 0, evening = 0, night = 0;
    cin >> num >> startHour >> startMin >> endHour >> endMin;
    int sMin = startHour*60 + startMin;
    int eMin = endHour*60 + endMin;
    sMin = (sMin+1) % 1440;
    eMin = (eMin+1) % 1440;
    if(sMin != eMin) {
        while(sMin != eMin) {
            if(sMin > 480 && sMin <= 1080) {
                day++;
            } else if(sMin > 1080 && sMin <= 1320) {
                evening++;
            } else {
                night++;
            }
            sMin = (sMin+1) % 1440;
        }
    } else {
        day = 600;
        evening = 240;
        night = 600;
    }
    
    double ans = table[cat-'A'][0]*day + table[cat-'A'][1]*evening + table[cat-'A'][2]*night;
    cout << setw(10) << num << setw(6) << day << setw(6) << evening << setw(6) << night << setw(3) << cat << setw(8) << fixed << setprecision(2) << ans << endl;
}

int main() {
    char cat;
    while(cin >> cat && cat != '#') {
        solve(cat);
    }
    system("pause");
}

```
