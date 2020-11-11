# [389 - Basically Speaking](https://onlinejudge.org/index.php?option=onlinejudge&Itemid=8&page=show_problem&problem=325)

## 題目概要

要你做一個能夠把n進制轉成m進制的程式，其中n, m介在整數2跟16之間

並且要注意幾點

- 總共要顯示7格的長度，低於7位數的要補空格並且向右對齊

- 大於9的數字用大寫字母 A B C...表示

- 超出範圍的要輸出ERROR(也要向右對齊)

## 解題過程

邊寫邊賭爛，輸出還要補空格真的很煩，不得不抱怨uva的某些IO是真的很煩人。我個人是通通都先轉成十進制，然後慢慢除，這題沒什麼，就是看能不能理解進制轉換而已。
(然後我的code很醜)





## AC程式碼

```c++
#include <bits/stdc++.h>
#define iss ios::sync_with_stdio(false)
using namespace std;

int myPow(int num, int p){
    if(p == 0){
        return 1;
    }
    int temp = num;
    for(int i = 1; i < p; ++i){
        num *= temp;
    }
    return num;
}

int main(){
    string str;
    string ans;
    int from;
    int to;
    int dec = 0;
    int biggestPow = 0;
    int temp;
    map<char, int> dict = {
        {'A', 10},
        {'B', 11},
        {'C', 12},
        {'D', 13},
        {'E', 14},
        {'F', 15},
        {'0', 0},
        {'1', 1},
        {'2', 2},
        {'3', 3},
        {'4', 4},
        {'5', 5},
        {'6', 6},
        {'7', 7},
        {'8', 8},
        {'9', 9}
    };
    map<int, char> dict2 = {
        {10, 'A'},
        {11, 'B'},
        {12,'C'},
        {13,'D'},
        {14,'E'},
        {15,'F'},
        {0,'0'},
        {1,'1'},
        {2,'2'},
        {3,'3'},
        {4,'4'},
        {5,'5'},
        {6,'6'},
        {7,'7'},
        {8,'8'},
        {9,'9'}
    };
    while(cin >> str){
        ans = "";
        dec = 0;
        biggestPow = 0;
        cin >> from;
        cin >> to;
        if(str == "0"){
            cout << setw(7) << 0 << endl;
            continue;
        }
        for(int i = str.length()-1, power = 0; i >= 0; --i, ++power){
            dec += dict[str[i]] * myPow(from, power);
        }
        if(to == 10){
            if(dec <= 9999999){
                cout << setw(7) << dec << endl;
                continue;
            }
            cout <<"  ERROR" << endl;
            continue;
            
        }
        while(myPow(to, biggestPow+1) <= dec){
            biggestPow++;
        }
        if(biggestPow >= 7){
            cout << "  ERROR" << endl;
            continue;
        }
        while(biggestPow != -1){
            temp = dec / myPow(to, biggestPow);
            dec -= temp * myPow(to, biggestPow);
            ans += dict2[temp];
            //cout << temp;
            biggestPow--;
        }
        cout << setw(7) << ans << endl;
    }
    
    system("pause");
    return 0;
}
```
