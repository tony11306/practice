#include <iostream>
#include <vector>
#include <set>
#include <fstream>
#include <iomanip>
#include <algorithm>
#include <utility>

using namespace std;

const int BOX_COUNT = 4;
set<string> candidatesName;


class Candidate {
    private:
        int boxes[BOX_COUNT] = {0};
        string name;

    public:

    Candidate(string name);
    int getTotal();
    void addVoteToBox(int boxIndex, int votes);
    string getName();
    int* getBoxes();
};

vector<Candidate> candidateList;

void vote(string name, int region, int votes) {
    for(int i = 0; i < candidateList.size(); ++i) {
        if(candidateList[i].getName() == name) {
            candidateList[i].addVoteToBox(region, votes);
            break;
        }
    }
}

pair<string, int> getWinner() {
    pair<string, int> winner("", -1); // name / votes
    for(int i = 0; i < candidateList.size(); ++i) {
        if(winner.second < candidateList[i].getTotal()) {
            winner = make_pair(candidateList[i].getName(), candidateList[i].getTotal());
        }
    }
    return winner;
}

void displayResult() {

    pair<string, int> winner = getWinner();
    int totalVotes = 0;

    cout << "           --------------Election Results--------------           " << endl;
    cout << "Candidate                       votes" << endl;
    cout << "Name        Region1   Region2   Region3   Region4     Total" << endl;
    cout << "---------   -------   -------   -------   -------   -------" << endl;
    for(int i = 0; i < candidateList.size(); ++i) {
        int* boxes = candidateList[i].getBoxes();
        printf("%-9s   %7d   %7d   %7d   %7d    %6d\n", candidateList[i].getName().c_str(), boxes[0], boxes[1], boxes[2], boxes[3], candidateList[i].getTotal());
        totalVotes += candidateList[i].getTotal();
    }
    cout << endl << endl;
    cout << "Winner: " << winner.first << ", Votes Received: " << winner.second << endl << endl;
    cout << "Total votes polled: " << totalVotes << endl;
}

bool comp(Candidate a, Candidate b) {
    int shorterNameLength = (a.getName().length() < b.getName().length()) ? (a.getName().length()) : (b.getName().length());
    for(int i = 0; i < shorterNameLength; ++i) {
        if(a.getName()[i] != b.getName()[i]) {
            return a.getName()[i] < b.getName()[i];
        }
    }
    return a.getName().length() < b.getName().length();
}




int main()
{
    fstream nameFileStream("name.txt");
    fstream dataFileSteam("data.txt");

    string name;

    while(nameFileStream >> name) { // 讀取候選人名單
        if(candidatesName.find(name) == candidatesName.end()) { // 如果沒有找到的話
            candidatesName.insert(name);
            Candidate newCandidate = Candidate(name);
            candidateList.push_back(newCandidate);
            // cout << newCandidate.getName() << endl;
        }
    }

    int region;
    int votes;
    while(dataFileSteam >> name >> region >> votes) {
        // cout << name << " " << region << " " << votes << endl;
        vote(name, region, votes);
    }
    sort(candidateList.begin(), candidateList.end(), comp);
    displayResult();

    return 0;
}



Candidate::Candidate(string name) {
    this->name = name;
}

void Candidate::addVoteToBox(int boxIndex, int votes) {
    if(boxIndex > BOX_COUNT || boxIndex <= 0) {
        return;
    }

    this->boxes[boxIndex-1] += votes;
}

int Candidate::getTotal() {
    int total = 0;
    for(int i = 0; i < BOX_COUNT; ++i) {
        total += this->boxes[i];
    }
    return total;
}

string Candidate::getName() {
    return this->name;
}

int* Candidate::getBoxes() {
    return this->boxes;
}
