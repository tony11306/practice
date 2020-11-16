# [10193 - All You Need Is Love](https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=1134)

## 題目概要

給你兩個二進制字串，只要兩者最大公因數是1就輸出"Love is not all you need!"，反之，則輸出"All you need is love"。

## 解題過程

痾，英文不好題目看很久，總之就是水到不能再水的題目。

## AC程式碼

```c++
#include <bits/stdc++.h>
#define ll long long
using namespace std;  

int main() {
    int cases;
    cin >> cases;
    for(int i = 0; i < cases; ++i) {
        string s1;
        string s2;
        int s1Value = 0;
        int s2Value = 0;
        cin >> s1 >> s2;
        for(int j = s1.length()-1; j >= 0; --j) {
            if(s1[j] == '1') {
                s1Value += pow(2, s1.length()-1 - j);
            }
        }
        for(int j = s2.length()-1; j >= 0; --j) {
            if(s2[j] == '1') {
                s2Value += pow(2, s2.length()-1 - j);
            }
        }
        if(__gcd(s1Value, s2Value) != 1){
            cout << "Pair #" << i+1 << ": All you need is love!\n";
        }else{
            cout << "Pair #" << i+1 << ": Love is not all you need!\n";
        }
        
    }
    system("pause");
    return 0;
    
}
```
