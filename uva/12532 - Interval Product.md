```c++
// 雖說是線段樹裸題(單點修改 區間查詢) 但我還是刻爆了 幹 直接貼模板過來了
// bit也可以的樣子 但我不會
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

class SegmentTreeNode{

    public:

        int sum;
        int startIndex;
        int endIndex;
        SegmentTreeNode* left = nullptr;
        SegmentTreeNode* right = nullptr;

        SegmentTreeNode(vector<int> &arr, int startI, int endI){
            if(startI < endI){
                int mid;
                this->startIndex = startI;
                this->endIndex = endI;
                mid = (endI + startI) / 2;

                this->left = new SegmentTreeNode(arr, startI, mid);
                this->right = new SegmentTreeNode(arr, mid + 1, endI);
            }else if(startI == endI){
                this->startIndex = startI;
                this->endIndex = endI;
                this->sum = arr[startI];
                return;
            }
            this->sum = this->left->sum * this->right->sum;
        }

        ~SegmentTreeNode() {
            if(left != nullptr) {
                delete left;
            } else if(right != nullptr) {
                delete right;
            }
        }

        void update(int index, int value){
            if(this->endIndex == index && this->startIndex == index){
                this->sum = value;
                return;
            }
            int mid = (this->startIndex + this->endIndex) / 2;
            if(index <= mid){
                this->left->update(index, value);
            }else{
                this->right->update(index, value);
            }
            this->sum = this->left->sum * this->right->sum;
        }

        int query(int startI, int endI){
            if(startI == this->startIndex && endI == this->endIndex){
                return this->sum;
            }
            int mid;
            long long int s = 1;
            mid = (this->endIndex + this->startIndex) / 2;

            if(startI > mid){
                return this->right->query(startI, endI);
            }else if(endI <= mid){
                return this->left->query(startI, endI);
            }else{
                s *= this->left->query(startI, mid);
                s *= this->right->query(mid+1, endI);
            }
            return s;
            
        }

};


void solve(int n, int m) {
    vector<int> arr(n);
    for(int i = 0; i < n; ++i) {
        cin >> arr[i];
        if(arr[i] > 0) {
            arr[i] = 1;
        } else if(arr[i] < 0) {
            arr[i] = -1;
        } else {
            arr[i] = 0;
        }
    }
    string ans = "";
    SegmentTreeNode segmentTree(arr, 0, n-1);
    while(m--) {
        char c;
        cin >> c;
        if(c == 'C') {
            int index, d;
            cin >> index >> d;
            if(d > 0) {
                d = 1;
            } else if(d < 0) {
                d = -1;
            } else {
                d = 0;
            }
            segmentTree.update(index-1, d);
        } else {
            int l, r;
            cin >> l >> r;
            int result = segmentTree.query(l-1,r-1);
            if(result > 0) {
                ans += "+";
            } else if(result < 0) {
                ans += "-";
            } else {
                ans += "0";
            }
        }
    }
    cout << ans << endl;
}

int main() {
    int n, m;
    while(cin >> n >> m) {
        solve(n, m);
    }
    system("pause");
}
```
