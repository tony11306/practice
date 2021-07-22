```c++
// 暴力剪枝 醜到靠杯 極限1.58s過關
#include<bits/stdc++.h>
#define ll long long
#define endl "\n"
#define dbg1(x) cout<<"Dbg--> "<<'['<<#x<<':'<<x<<']'<<endl
#define dbg2(x,y) cout<<"Dbg--> "<<'['<<#x<<':'<<x<<' '<<#y<<':'<<y<<']'<<endl
#define dbg3(x,y,z) cout<<"Dbg--> "<<'['<<#x<<':'<<x<<' '<<#y<<':'<<y<<' '<<#z<<':'<<z<<']'<<endl
#define FOR_EACH_CASE(x) for(int cas = 1; cas <= x && (cout << "Case " << cas << ": "); ++cas)
#define iss std::ios::sync_with_stdio(0);std::cin.tie(0)
using namespace std; 

void solve() {
    string s;
    cin >> s;
    int chars[26] = {0};
    for(char c : s) {
        chars[c-'A']++;
    }
    set<string> ans;
    set<char> indexOneSet;
    
    set<char> allChar(s.begin(), s.end());
    for(int i = 0; i < s.length(); ++i) {
        set<char> indexTwoSet;
        if(indexOneSet.size() == allChar.size()) {
            break;
        } else if(indexOneSet.find(s[i]) != indexOneSet.end()) {
            continue;
        }
        
        if(chars[s[i]-'A'] <= 0) {
            continue;
        }
        string current1 = "";
        current1 += s[i];
        indexOneSet.insert(s[i]);
        
        for(int j = i+1; j < s.length(); ++j) {
            set<char> indexThreeSet;
            if(indexTwoSet.size() == allChar.size()) {
                break;;
            } else if(indexTwoSet.find(s[j]) != indexTwoSet.end()) {
                continue;
            }
            if(s[i] == s[j]) {
                if(chars[s[j]-'A']-1 <= 0) {
                    continue;
                }
            } else if(chars[s[j]-'A'] <= 0) {
                continue;
            }
            string current2 = current1 + s[j];
            indexTwoSet.insert(s[j]);
            for(int k = j+1; k < s.length(); ++k) {
                
                if(indexThreeSet.size() == allChar.size()) {
                    break;
                } else if(indexThreeSet.find(s[k]) != indexThreeSet.end()) {
                    continue;
                }

                if(s[i] == s[k] && s[j] == s[k]) {
                    if(chars[s[k]-'A']-2 <= 0) {
                        continue;
                    }
                } else if(s[i] == s[k] || s[j] == s[k]) {
                    if(chars[s[k]-'A']-1 <= 0) {
                        continue;
                    }
                } else if(chars[s[k]-'A'] <= 0) {
                    continue;
                }
                indexThreeSet.insert(s[k]);
                string current3 = current2 + s[k];
                ans.insert(current3);
            }
        }
    }
    cout << ans.size() << endl;
}

int main() {
    int n;
    cin >> n;
    while(n--) {
        solve();
    }
}
```
