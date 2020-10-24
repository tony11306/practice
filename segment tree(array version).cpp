#include <bits/stdc++.h>
#define iss ios::sync_with_stdio(false)
using namespace std;

/**
 * @param start (int) arr's start position, usually starts from 0.
 * @param end   (int) arr's end position, usally end up with the arr.size() - 1.
 * @param nodeIndex (int) set it as 0, this value will change while recursing. It's the current index of the segmentTree.
 * 
 */
void buildSegmentTree(vector<int> &segmentTree, vector<int> &arr, int start, int end, int nodeIndex){
    if(start == end){
        segmentTree[nodeIndex] = arr[start];
        return;
    }
    int leftNode  = (2 * nodeIndex) + 1;
    int rightNode = (2 * nodeIndex) + 2;
    int mid = (end + start) / 2;

    buildSegmentTree(segmentTree, arr, start, mid, leftNode);
    buildSegmentTree(segmentTree, arr, mid+1, end, rightNode);
    segmentTree[nodeIndex] = segmentTree[leftNode] + segmentTree[rightNode];
}

/**
 * @param start (int) arr's start position, usually starts from 0.
 * @param end   (int) arr's end position, usally end up with the arr.size() - 1.
 * @param L     (int) the query interval left.
 * @param R     (int) the query interval right.
 * @param nodeIndex (int) set it as 0, this value will change while recursing. It's the current index of the segmentTree.
 *  
 */
int query(vector<int> &segmentTree, vector<int> &arr, int start, int end, int L, int R, int nodeIndex){
    
    if(start > R || L > end){
        return 0;
    }else if(L <= start && end <= R){
        return segmentTree[nodeIndex];
    }

    int leftNode  = (nodeIndex * 2) + 1;
    int rightNode = (nodeIndex * 2) + 2;
    int mid = (end + start) / 2;
    int leftSum = query(segmentTree, arr, start, mid, L, R, leftNode);
    int rightSum = query(segmentTree, arr, mid+1, end, L, R, rightNode);
    return leftSum + rightSum;
    

}

/**
 * @param start (int) arr's start position, usually starts from 0.
 * @param end   (int) arr's end position, usally end up with the arr.size() - 1.
 * @param targetIndex (int) the index you wanna update in arr.
 * @param value (int) the value you wanna update at arr[targetIndex].
 * @param nodeIndex (int) set it as 0, this value will change while recursing. It's the current index of the segmentTree.
 * 
 */

void update(vector<int> &segmentTree, vector<int> &arr, int start, int end, int targetIndex, int value, int nodeIndex){
    if(start == targetIndex && end == targetIndex){
        arr[targetIndex] = value;
        segmentTree[nodeIndex] = value;
        return;
    }
    int leftNode  = (nodeIndex * 2) + 1;
    int rightNode = (nodeIndex * 2) + 2;
    int mid = (start + end) / 2;
    if(targetIndex <= mid){
        update(segmentTree, arr, start, mid, targetIndex, value, leftNode);
    }else{
        update(segmentTree, arr, mid+1, end, targetIndex, value, rightNode);
    }
    segmentTree[nodeIndex] = segmentTree[leftNode] + segmentTree[rightNode];

}

int main(){
    vector<int> arr = {1,5,8,4,2,5};
    vector<int> segmentTree(arr.size() * 4);
    int treeSize = arr.size() * 4;
    int start = 0;
    int end = arr.size() - 1;
    buildSegmentTree(segmentTree, arr, start, end, 0);
    
    update(segmentTree, arr, 0, arr.size()-1, 4, 20, 0);
    for(int i = 0; i < segmentTree.size(); ++i){
        printf("segmentTree[%d] = %d\n", i, segmentTree[i]);
    }
    cout << query(segmentTree, arr, 0, arr.size()-1, 1, 5, 0);
    system("pause");
    return 0;
}
