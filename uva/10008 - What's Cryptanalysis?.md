# [10008 - What's Cryptanalysis?](https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=949)

## 題目概要

就是統計英文字母出現的次數而已 ~水到不能再水的題目~

第一行輸入n, 代表有n行，接下來的n行字串，統計英文字母出現的次數(小寫大寫都算同一個，可能會有不是英文字母的，要注意)

## 解題過程

痾，map開下去，然後sort就好

## AC程式碼

```c++
#include <bits/stdc++.h>
#define ll long long
using namespace std;  

bool compare(pair<char, int> p1, pair<char, int> p2){
    return p1.second > p2.second;
}

int main() {
    int lines;
    cin >> lines;
    cin.ignore();
    map<char, int> table;
    for(int i = 0; i < lines; ++i){
        string s;
        getline(cin, s);
        for(int j = 0; j < s.length(); ++j){
            if(s[j] >= 97 && (int)s[j] <= 122){
                table[s[j]-32]++;
            }else if(s[j] >= 65 && s[j] <= 90){
                table[s[j]]++;
            }
        }
    }
    vector<pair<char, int>> sortMap;
    for(map<char, int>::iterator it = table.begin(); it != table.end(); ++it){
        sortMap.push_back(make_pair(it->first, it->second));
    }
    sort(sortMap.begin(), sortMap.end(), compare);
    for(int i = 0; i < sortMap.size(); ++i){
        cout << sortMap[i].first << " " << sortMap[i].second << "\n";
    }
    system("pause");
    return 0;
    
}

```
