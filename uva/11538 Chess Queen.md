# [11538 - Chess Queen](https://onlinejudge.org/index.php?option=onlinejudge&Itemid=8&page=show_problem&category=0&problem=2533&)

## 題目概要

給你一個m*n的棋盤，找出皇后棋可以攻擊的排列組合有幾種。而皇后棋在同行或同列或同對角線時可以攻擊。

## 解題過程

基本上是一個純數學題，但是我搞了一整天都沒解出來，一方面是自己數學邏輯概念太差，想很久才寫出來，而且寫出來的還不是純數學解，還有用到迴圈。另一方面最後講。

    可以把問題分解成三部分，所有列的排列組合 + 所有行的排列組合 + 所有對角線的排列組合。

列行絕對不是問題，只要高中有學過基礎的排組都知道，主要是對角線需要一點觀察，首先長的我叫a 短的我叫b，那麼有長度為b格的對角線就有(a-b+1)*2個，而剩下的則是1到b-1長度的對角線(每一個長度
都有4條，對應到4個角落)。接著把這三個加起來就是答案了

我剛剛有提到另一個方面，主要是我一開始把a和b設定成int，ans設成long long，結果debug了一整天，後來才發現我一開始就有錯

    ans += a*(b*(b-1)) + b*(a*(a-1));
    
等號右邊的+號，可以發現兩邊都是int的型別，這樣會導致先把結果用int計算，然後再加上ans，會有溢位的問題，後來a b，改成long long就過了 ==

## AC程式碼

```c++
#include <bits/stdc++.h>
using namespace std;

long long p(long long a, long long b){
    long long val = 1;
    if(a == 1){
        return 0;
    }
    for(int cnt = 0; cnt < b; ++cnt, --a){
        val *= a;
    }
    return val;
}

int main(){
    long long a, b;
    while(cin >> a >> b){
        if(a == 0 && b == 0){
            break;
        }
        if(b > a){
            swap(a, b);
        }
        // a大 b小
        long long ans = 0;
        ans += a*(b*(b-1)) + b*(a*(a-1));
        for(int i = 1; i <= a; ++i){
            if(i >= b){
                ans += p(b, 2)*2;
                continue;
            }
            ans += p(i, 2)*4;
        }
        cout << ans << "\n";
    }
    system("pause");
    return 0;
}
```
