#include <bits/stdc++.h>
using namespace std;

void initDet(vector< vector<long long int> > &det, int detSize){
    det.resize(detSize);
    for(int i = 0; i < detSize; ++i){
        det[i].resize(detSize);
    }
}

long long int getDetValue(vector< vector<long long int> > &det, int detSize){

    if(detSize == 1){
        return det[0][0];
    }
    vector< vector<long long int> > cofactor;
    initDet(cofactor, detSize-1);
    long long int value = 0;
    for(int i = 0; i < detSize; ++i){
        for(int j = 1; j < detSize; ++j){
            for(int k = 0, a = 0; k < detSize; ++k){
                if(k != i){
                    cofactor[j-1][a] = det[j][k];
                    a++;
                }
            }
        }
        if(i&1){ // i is odd
            value += -1*det[0][i]*getDetValue(cofactor, detSize-1);

        }else{ // i is even
            value += 1*det[0][i]*getDetValue(cofactor, detSize-1);
        }
    }

    return value;

}

int main()
{
    int detSize;
    vector< vector<long long int> > det;

    cin >> detSize;
    initDet(det, detSize);
    for(int i = 0; i < det.size(); ++i){
        for(int j = 0; j < det[i].size(); ++j){
            cin >> det[i][j];
        }
    }
    long long int value = getDetValue(det, detSize);
    cout << value << endl;

    return 0;
}
