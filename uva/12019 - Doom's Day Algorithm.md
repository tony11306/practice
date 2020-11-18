# [12019 - Doom's Day Algorithm](https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=3170)

## 題目概要

已知2011年的4/4, 6/6, 8/8, 10/10, 12/12都為Monday，題目會輸入n行資料，每行兩整數，分別代表月和日，要你輸出那天是禮拜幾。

## 寫題過程

~每日一水題 達成~ 不是很清楚這一題的原意是要我們怎麼寫，我想說日期都給出來哪一天是禮拜幾了，而且還固定在2011年，所以我就直接建表了。

## AC程式碼

```c++
#include <bits/stdc++.h>
#define ll long long
using namespace std;  

int main() {
    // 2011 year 建表
    vector<string> dates = {"Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"};
    int datesPointer = 4;
    map<int, map<int, string>> table;
    for(int i = 4; i <= 12; ++i){
        int days = (i == 4 || i == 6 || i == 9 || i == 11) ? 30 : 31;
        for(int j = 1; j <= days; ++j){
            table[i][j] = dates[datesPointer];
            datesPointer = (datesPointer == 6) ? 0 : datesPointer + 1;
        }
    }
    datesPointer = 3;
    for(int i = 3; i > 0; --i){
        int days = (i == 2) ? 28 : 31;
        for(int j = days; j > 0; --j){
            
            table[i][j] = dates[datesPointer];
            datesPointer = (datesPointer == 0) ? 6 : datesPointer - 1;
        }
    }
    
    int cases;
    cin >> cases;
    int m, d;
    for(int i = 0; i < cases; ++i){
        cin >> m >> d;
        cout << table[m][d] << "\n";
    }
    system("pause");
    return 0;
    
}


```
