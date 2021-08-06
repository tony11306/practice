#include <bits/stdc++.h>
using namespace std;

class SegmentTreeNode{

    public:

        long long int sum;
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
            this->sum = this->left->sum + this->right->sum;
            //cout << startI << "-" << endI << ":" << this->sum << endl;
            
        }
    
        ~SegmentTreeNode() {
            if(left != nullptr) {
                delete left;
            }
            if(right != nullptr) {
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
            this->sum = this->left->sum + this->right->sum;
        }

        long long int query(int startI, int endI){
            if(startI == this->startIndex && endI == this->endIndex){
                return this->sum;
            }
            //cout << startI << "/" << this->startIndex << " " << endI << "/" << this->endIndex << endl;
            int mid;
            long long int s = 0;
            mid = (this->endIndex + this->startIndex) / 2;

            if(startI > mid){
                return this->right->query(startI, endI);
            }else if(endI <= mid){
                return this->left->query(startI, endI);
            }else{
                s += this->left->query(startI, mid);
                s += this->right->query(mid+1, endI);
            }
            return s;
            
        }

};

int main(){
    vector<int> arr;
    for(int i = 0; i < 12; ++i){
        arr.push_back(i);
    }
    SegmentTreeNode* segmentTree = new SegmentTreeNode(arr, 0, 11);
    segmentTree->update(3,100); 
    cout << segmentTree->query(3,5); // output: 109
    system("pause");
    return 0;
}
