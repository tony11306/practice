這題還滿不錯的，原本以為想出來的方法O(n)應該可以了，結果還是TLE了。

基本上這題就是求 2~n 的所有數字的因數和。把表列出來可以發現 1 的出現次數為 `floor(n/1)` 次，2 出現的次數為 `floor(n/2)` 次...以此類推，所以我一開始是寫 `for 2~n: ans += (n/i) * i` O(n)。

結果當然是 TLE 了，想了很久還是不會優化，就直接查了。這題我到這邊其實已經對一半了，仔細觀察可以發現 2 ~ N 的出現次數是遞減的，而且某些數字的出現次數會重複，所以我們可以利用某種方式來加速我們的 i 移動，假設 `N = 10`, `i = 4`，
這時 `4` 的出現次數為 `floor(10/4) == 2`次，而 `10 / 2 = 5` ，代表最後一個出現兩次的數字是 `5`，到這邊就可以利用等差數列的公式算出 `4 + 5 = (4 + 5) * 2 / 2 = 9`，然後 `9 * 2 = 18`，
這邊的意思是我們算出了`4`跟`5`的出現次數並加總起來，接著就 `ans += 18` 了，
由於 5 的結果算完了，所以我們可以把 i 加速到 6，當 N 很大時，這個加速就非常有感了。


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

int n;
int main() {
    
    while(cin >> n && n != 0) {

        ll ans = 0;
        for(ll l = 1, r; l <= n;) { // 左區間為 i
            r = n/(n/l);
            ans += ((l+r) * (r-l+1) / 2) * (n/l);
            l = r + 1;
        }
        cout << ans-1 << endl;
    }
    system("pause");
}
```
