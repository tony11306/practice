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
const int INF = ~(1<<31);
const int INF_0x3f = 0x3f3f3f3f;

bool isAllowed(int king, int queen) {
    if(king/8 != 0 && king-8 == queen) {
        return false;
    }
    if(king/8 != 7 && king+8 == queen) {
        return false;
    }
    if(king%8 != 0 && king-1 == queen) {
        return false;
    }
    if(king%8 != 7 && king+1 == queen) {
        return false;
    }
    return true;
}

bool isStalemate(int king, int queen) {
    if(king == 0 && queen == 9) {
        return true;
    }
    if(king == 7 && queen == 14) {
        return true;
    }
    if(king == 56 && queen == 49) {
        return true;
    }
    if(king == 63 && queen == 54) {
        return true;
    }
    return false;
}

void solve(int king, int qFrom, int qTo) {

    if(king == qFrom) {
        cout << "Illegal state" << endl;
        return;
    }

    if(qTo == king || qFrom == qTo) {
        cout << "Illegal move" << endl;
        return;
    } else if(abs(qTo-qFrom) % 8 == 0) {
        if(qTo % 8 == king % 8 && qFrom % 8 == king % 8) {
           if(min({qTo, qFrom, king}) != king && max({qTo, qFrom, king}) != king) {
                cout << "Illegal move" << endl;
                return;
            } 
        }
        
    } else if(qFrom / 8 == qTo / 8) {
        if(qFrom / 8 == king / 8) {
            if(min({qTo, qFrom, king}) != king && max({qTo, qFrom, king}) != king) {
                cout << "Illegal move" << endl;
                return;
            }
        }
        
    } else if(abs(qTo-qFrom) % 8 != 0 && qFrom / 8 != qTo / 8) {
        cout << "Illegal move" << endl;
        return;
    }

    if(!isAllowed(king, qTo)) {
        cout << "Move not allowed" << endl;
        return;
    }

    if(!isStalemate(king, qTo)) {
        cout << "Continue" << endl;
        return;
    }

    cout << "Stop" << endl;
}

int main() {
    int king;
    int qFrom;
    int qTo;
    while(cin >> king >> qFrom >> qTo) {
        solve(king, qFrom, qTo);
    }
    system("pause");
}
```
