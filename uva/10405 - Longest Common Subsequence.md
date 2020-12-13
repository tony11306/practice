# [10405 - Longest Common Subsequence](https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=9)

## 題目概要

給你兩字串，要你找最長公共子序列(LCS)，注意測資會有空白行喔。

## 解題過程

裸LCS題目，不過我是第一次寫LCS題目，想當然爾，我想不出來，只好跑去看[演算法筆記](http://web.ntnu.edu.tw/~algo/LongestCommonSubsequence.html)，感謝裡面詳細的講解，
我才勉強把這題寫出來。我的code基本上都是抄這裡的code啦，所以直接看點連結去那邊看比較快

## AC程式碼

```c++
#include <bits/stdc++.h>
using namespace std;

int main(){
    string s1;
    string s2;
    while(getline(cin, s1)){
        getline(cin, s2);
        if(s2.length() > s1.length()){
            swap(s1, s2);
        }
        int dp[s1.length()+1][s2.length()+1]; // [前i個元素][前j個元素]
        for(int i = 0; i <= s1.length(); ++i){
            dp[i][0] = 0;
        }
        for(int i = 0; i <= s2.length(); ++i){
            dp[0][i] = 0;
        }
        memset(dp, 0, sizeof(dp));
        int ans = 0;
        for(int i = 1; i <= s1.length(); ++i){
            for(int j = 1; j <= s2.length(); ++j){
                if(s1[i-1] == s2[j-1]){
                    dp[i][j] = dp[i-1][j-1]+1;
                }else{
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1]);
                }
                ans = max(ans, dp[i][j]);
            }
        }
        cout << ans << "\n";
    }
    system("pause");
    return 0;
}
```
