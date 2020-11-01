# [10267-Graphical Editor](https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=1208)

## 題目概要

如同題目所述，你的目標是製作一個簡單的圖案編輯器，編輯器要有以下功能:


注意 以下我提的 M x N 表格座標將會是這樣

```
(1,1), (1,2), (1,3), ...., (1,M) → X

(2,1), (2,2), (2,3), ...., (2,M)

.       .      .      .     .

.       .      .      .     .

.       .      .      .     .

(N,1), (N,2), (N,3), ...., (N,M)

↓
Y
```




<table width="50%">
    <tr>
        <td>指令使用方法</td>
        <td>說明</td>
    </tr>
    <tr>
        <td>I M N</td>
        <td>建立一個 M x N 大小的表格，表格預設內容全部為大寫英文字母 O。</td>
    </tr>
    <tr>
        <td>C</td>
        <td>把所有表格內的內容全部重設為 大寫英文字母 O。 (表格大小不變)</td>
    </tr>
    <tr>
        <td>L X Y C</td>
        <td>把座標(X, Y)的點改成顏色 C。</td>
    </tr>
    <tr>
        <td>V X Y1 Y2 C</td>
        <td>選定橫軸的第X個點後，把(X, Y1)到(X, Y2)都改成顏色C。 (注意: Y1跟Y2的大小是不一定的)</td>
    </tr>
    <tr>
        <td>H X1 X2 Y C</td>
        <td>選定縱軸的第Y個點後，把(X1, Y)到(X2, Y)都改成顏色C。 (注意: X1跟X2的大小是不一定的)</td>
    </tr>
    <tr>
        <td>K X1 Y1 X2 Y2 C</td>
        <td>把(X1, Y1)和(X2, Y2)所圍成的矩形都改成顏色C。 (注意: X1跟X2 和 Y1跟Y2的大小是不一定的)</td>
    </tr>
    <tr>
        <td>F X Y C</td>
        <td>
        <div style="width: 50pt">把一個同一個region的顏色都改成 C。 給定一個點(X,Y)，假設此點顏色為W，若四周某一個點的顏色也是W，則那點和(X,Y)為同一個region，而那點又能再向四周偵測，若有同顏色的點，那麼region又會繼續擴大，以此類推。 (我知道我講得不太好，總之就是你開小畫家，畫一個圈，選油漆桶，然後點圈內某一點，出來的結果就是我要講的概念)</div>
        </td>
    </tr>
    <tr>
        <td>S name</td>
        <td>列印出name，並且在換行後列印出目前圖案的樣子。</td>
    </tr>
    <tr>
        <td>X</td>
        <td>程式終止。</td>
    </tr>
</table>

~表格跑掉了，我不會調，去看原文吧~

## 解題過程

~草尼瑪怎麼這麼麻煩 CPE考這題我是要怎麼寫完~

題目本身不難理解，就是實作上很煩，頂多就油漆桶那邊需要用到一點DFS或BFS的概念。

不過坐標軸寫到很混亂，寫過俄羅斯方塊後的我依舊會亂掉，debug時可以往這方向去檢查。

還有我的input技巧可能還要再改進，這麼多atoi感覺就礙眼。

## AC程式碼

```c++
#include <bits/stdc++.h>
using namespace std;

vector<string> split(string s){
    istringstream is(s);
    vector<string> stringArr;
    string subString;
    while(getline(is, subString, ' ')){
        stringArr.push_back(subString);
    }
    return stringArr;
}

void swap(int &a, int &b){
    a ^= b;
    b ^= a;
    a ^= b;
}

bool isOutside(int tableX, int tableY, int currentX, int currentY){
    if(currentX > tableX || currentX <= 0){
        return true;
    }else if (currentY > tableY || currentY <= 0){
        return true;
    }
    return false;
}

void dfsFill(vector< vector<char> > &table, int currentX, int currentY, char color, char region){
    if(color == region){
        return;
    }
    table[currentX-1][currentY-1] = color;
    pair<int, int> up(currentX, currentY+1);
    pair<int, int> down(currentX, currentY-1);
    pair<int, int> left(currentX-1, currentY);
    pair<int, int> right(currentX+1, currentY);
    if(!isOutside(table.size(), table[0].size(), up.first, up.second) && table[up.first-1][up.second-1] == region){
        dfsFill(table, up.first, up.second, color, region);
    }
    if(!isOutside(table.size(), table[0].size(), down.first, down.second) && table[down.first-1][down.second-1] == region){
        dfsFill(table, down.first, down.second, color, region);
    }
    if(!isOutside(table.size(), table[0].size(), left.first, left.second) && table[left.first-1][left.second-1] == region){
        dfsFill(table, left.first, left.second, color,region);
    }
    if(!isOutside(table.size(), table[0].size(), right.first, right.second) && table[right.first-1][right.second-1] == region){
        dfsFill(table, right.first, right.second, color, region);
    }
    
}

int main(){
    vector< vector<char> > table;
    string fileName = "";
    string commandLine = "";
    vector<string> splitString;
    while(getline(cin, commandLine)){
        splitString = split(commandLine);
        int x1, y1, x2, y2;
        char color;
        char region;
        switch(splitString[0][0]){

            case 'I':
                int m, n;
                m = atoi(splitString[1].c_str());
                n = atoi(splitString[2].c_str());
                table.clear();
                for(int i = 0; i < n; ++i){
                    vector<char> newArr;
                    table.push_back(newArr);
                    for(int j = 0; j < m; ++j){
                        table[i].push_back('O');
                    }
                }
                break;

            case 'C':
                for(int i = 0; i < table.size(); ++i){
                    for(int j = 0; j < table[i].size(); ++j){
                        table[i][j] = 'O';
                    }
                }
                break;
            
            case 'L':
                x1 = atoi(splitString[1].c_str());
                y1 = atoi(splitString[2].c_str());
                color = splitString[3][0];
                table[y1-1][x1-1] = color;
                break;
            
            case 'V':
                x1 = atoi(splitString[1].c_str());
                y1 = atoi(splitString[2].c_str());
                y2 = atoi(splitString[3].c_str());
                color = splitString[4][0];
                if(y1 > y2){
                    swap(y1, y2);
                }
                for(int i = y1; i <= y2; ++i){
                    table[i-1][x1-1] = color;
                }
                break;

            case 'H':
                x1 = atoi(splitString[1].c_str());
                x2 = atoi(splitString[2].c_str());
                y1 = atoi(splitString[3].c_str());
                color = splitString[4][0];

                if(x1 > x2){
                    swap(x1, x2);
                }

                for(int i = x1; i <= x2; ++i){
                    table[y1-1][i-1] = color;
                }
                break;

            case 'K':
                x1 = atoi(splitString[1].c_str());
                y1 = atoi(splitString[2].c_str());
                x2 = atoi(splitString[3].c_str());
                y2 = atoi(splitString[4].c_str());
                color = splitString[5][0];
                if(x1 > x2){
                    swap(x1, x2);
                }
                if(y1 > y2){
                    swap(y1, y2);
                }
                for(int i = x1; i <= x2; ++i){
                    for(int j = y1; j <= y2; ++j){
                        table[j-1][i-1] = color;
                    }
                }
                break;

            case 'F':
                x1 = atoi(splitString[1].c_str());
                y1 = atoi(splitString[2].c_str());
                color = splitString[3][0];
                region = table[y1-1][x1-1];
                dfsFill(table, y1, x1, color, region);
                break;
            
            case 'S':
                fileName = splitString[1];
                cout << fileName << endl;
                for(int i = 0; i < table.size(); ++i){
                    for(int j = 0; j < table[i].size(); ++j){
                        cout << table[i][j];
                    }
                    cout << endl;
                }
                
                break;
            
            case 'X':
                system("pause");
                return 0;

            default:
                break;
        }
    }
    system("pause");
    return 0;
}

```
