[615 - Is It A Tree?](https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=556)
=============
## 題目概要
給你一堆邊，要你判斷這是不是一棵樹。

每兩個數字為一條邊，例如:a b，表示從a到b的邊。

下面是我已經整理過並且需要注意的點。

符合一棵樹的條件:
- 擁有唯一的根節點，並且有路徑可以從根節點開始走到每個在樹裡的節點
- 除了根節點，每一個樹節點，都只能被一個節點指到
- 不能有迴路的情況出現(cycle)

## 寫的過程
這題應該是我第一次寫的圖論題吧，原本看到pdf就想放棄，不過看到Tree就覺得好像是可以寫寫看的題目，同時也能練習一下STL的用法。

I/O我就不說了，我是先從第二點開始做，創造一個`map<int, vector<int>>`，key值是node，而value是有誰指向這個node。只要這個map裡某個value的size大於1就代表有重複指的情況出現。

第二點解決後，我就卡在一三點卡了一段時間，不是沒想法，是想不到怎麼實作，最後應該是用了最暴力的想法吧。首先，我們的map的key是不會存到root的，root只會存在於value裡，因為root沒有東西指向他，所以我就利用這個點，
loop過整個map的key，並且利用value一直往前找父節點，直到抵達root，這時把root存到`set<int> rootSet`裡面，為什麼要存到rootSet裡面?這是為了最後檢查root是否只有一個，
不然會出現**森林**的情況(多棵樹)。

最後剩下cycle，cycle判斷就簡單了，寫一個`set<int> visitedNode`，在每次往前找父節點的時候都把當前的node存到visitedNode裡面，並且檢查當前node有沒有在visitedNode裡面就行了。
## AC程式碼
```c++
#include <bits/stdc++.h>
#define iss ios::sync_with_stdio(false)
using namespace std;


bool isTree(map< int, vector<int> > &edges){
    set<int> rootSet;
    for(map< int, vector<int> >::iterator it = edges.begin(); it != edges.end(); ++it){
        set<int> visitedNode;
        int current = it->first;
        if(edges[it->first].size() > 1){
            return false;
        }
        while(true){
            if(edges.count(current) == 0){
                rootSet.insert(current);
                break;
            }else if(visitedNode.count(current) >= 1){
                return false;
            }
            visitedNode.insert(current);
            current = edges[current][0];
            
        }
    }
    if(rootSet.size() > 1){
        return false;
    }
    return true;

}

int main(){
    map< int, vector<int> > edges;
    int a, b;
    int caseCount = 1;
    while(cin >> a >> b){
        if(a == 0 && b == 0){
            if(isTree(edges)){
                printf("Case %d is a tree.\n", caseCount);
            }else{
                printf("Case %d is not a tree.\n", caseCount); 
            }
            caseCount++;
            edges.clear();
            continue;
        }else if(a < 0 && b < 0){
            break;
        }
        edges[b].push_back(a);
    }
    system("pause");
    return 0;
}
```
