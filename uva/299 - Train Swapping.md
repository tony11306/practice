```c++
#include<bits/stdc++.h>
#define ll long long
#define endl "\n"
#define dbg1(x) cout<<"Dbg--> "<<'['<<#x<<':'<<x<<']'<<endl
#define dbg2(x,y) cout<<"Dbg--> "<<'['<<#x<<':'<<x<<' '<<#y<<':'<<y<<']'<<endl
#define dbg3(x,y,z) cout<<"Dbg--> "<<'['<<#x<<':'<<x<<' '<<#y<<':'<<y<<' '<<#z<<':'<<z<<']'<<endl
#define ALL(x) x.begin(), x.end()
#define FOR_EACH_CASE(x) for(int cas = 1; cas <= x && (cout << "Case #" << cas << ": "); ++cas)
#define iss std::ios::sync_with_stdio(0);std::cin.tie(0)
using namespace std;
const int INF = ~(1<<31);
const int INF_0x3f = 0x3f3f3f3f;

int bubbleSort(int* arr, int n) {
    int ans = 0;
    for(int i = 0; i < n; ++i) {
        for(int j = 1; j < n-i; ++j) {
            if(arr[j-1] > arr[j]) {
                swap(arr[j-1], arr[j]);
                ans++;
            }
        }
    }
    return ans;
}

void solve() {
    int n;
    cin >> n;
    int arr[n];
    for(int i = 0; i < n; ++i) {
        cin >> arr[i];
    }

    cout << "Optimal train swapping takes "+ to_string(bubbleSort(arr, n)) +" swaps." << endl;


}

int main() {
    int n;
    cin >> n;
    while(n--) {
        solve();
    }
    system("pause");
}

```
