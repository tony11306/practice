```c++
// 馬的 我忘記 分 度 弧度 的關係，這題太吃數學了吧
// 第一次遇到要用三角函數的題目
#include<bits/stdc++.h>
#define ll long long
#define endl "\n"
#define dbg1(x) cout<<"Dbg--> "<<'['<<#x<<':'<<x<<']'<<endl
#define dbg2(x,y) cout<<"Dbg--> "<<'['<<#x<<':'<<x<<' '<<#y<<':'<<y<<']'<<endl
#define dbg3(x,y,z) cout<<"Dbg--> "<<'['<<#x<<':'<<x<<' '<<#y<<':'<<y<<' '<<#z<<':'<<z<<']'<<endl
#define FOR_EACH_CASE(x) for(int cas = 1; cas <= x && (cout << "Case " << cas << ": "); ++cas)
#define iss std::ios::sync_with_stdio(0);std::cin.tie(0)
using namespace std;
const int INF = ~(1<<31);
const int INF_0x3f = 0x3f3f3f3f;

int main() {
    int a, b;
    string s;
    while(cin >> a >> b >> s) {
        a += 6440;
        if(s == "deg") {
            if(b % 180 == 0 && b % 360 != 0) {
                b = 180;
            } else {
                if(b%360 > 180) {
                    b = 360 - b%360;
                } else {
                    b %= 180;
                }
            }
            cout << fixed << setprecision(6) << b*M_PI/180*a << " ";
            cout << fixed << setprecision(6) << sqrt(a*a+a*a-2*a*a*cos(b*M_PI/180)) << endl;
        } else {
            if(b % 10800 == 0 && b % 21600 != 0) {
                b = 10800;
            } else {
                if(b%21600 > 10800) {
                    b = 21600 - b%21600;
                } else {
                    b %= 10800;
                }
            }
            cout << fixed << setprecision(6) << b*M_PI/180/60*a << " ";
            cout << fixed << setprecision(6) << sqrt(a*a+a*a-2*a*a*cos(b*M_PI/180/60)) << endl;
        }
    }
    system("pause");
}

```
