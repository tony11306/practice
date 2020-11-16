# [10189 - Minesweeper](http://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=24&page=show_problem&problem=1130)

## 題目概要

給你一個n*m的二維陣列，'.' 代表安全區，'*'代表地雷。要你輸出一般踩地雷的格子樣子(周圍8格有k個地雷，那麼那格就是k)，若那格為地雷，則輸出'*'。

例如:

input:

  \* . . \*
  
  . . \* .
  
  . . . .
  
  . . . \*
  
output:

  \*12\*
  
  12\*2
  
  0122
  
  001\*
  
## 解題過程

水題，每格都檢查九宮格，輸出幾格地雷，就這樣而已。

## AC程式碼

```c++
#include <bits/stdc++.h>
#define ll long long
using namespace std;  

vector<vector<char>> initGameArea(int height, int width) {
    vector<vector<char>> area;
    for(int i = 0; i < height; ++i) {
        area.push_back(vector<char>(width));
        for(int j = 0; j < width; ++j) {
            cin >> area[i][j];
        }
        
    }
    return area;
}

char getAdjacentMines(vector<vector<char>> area, int x, int y) {
    if(area[x][y] == '*') {
        return '*';
    }
    int mines = 0;
    for(int i = x-1; i <= x+1; ++i) {
        for(int j = y-1; j <= y+1; ++j) {
            if(i == x && j == y){
                continue;
            }else if(i < 0 || j < 0 || i >= area.size() || j >= area[i].size()) {
                continue;
            }
            
            if(area[i][j] == '*') {
                mines++;
            }
        }
    }
    return mines + '0';
}

int main() {
    int height;
    int width;
    int fieldCount = 1;
    while(cin >> height >> width) {
        if(height == 0 && width == 0) {
            break;
        }else if(fieldCount != 1){
            cout << "\n";
        }
        vector<vector<char>> gameArea = initGameArea(height, width);
        cout << "Field #" << fieldCount << ":\n";
        for(int i = 0; i < height; ++i) {
            for(int j = 0; j < width; ++j) {
                cout << getAdjacentMines(gameArea, i, j);
            }
            cout << "\n";
        }
        fieldCount++;
    }
    system("pause");
    return 0;
    
}
```
