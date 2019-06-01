#include <iostream>
#include <vector>
#include <set>
using namespace std;
set<vector<int>> generate_powerset(vector<int> given) {
    if(given.size() == 0) {
        set<vector<int>> s_;
        s_.insert((vector<int>)-99);
        return s_;
    }
    else {
        set<vector<int>> s;
        s.insert(given);
        int elem = given.at(given.size() - 1);
        s.insert(vector<int>(elem));
        given.pop_back();
        set<vector<int>> s2 = generate_powerset(given);
        s.insert(s2.begin(), s2.end());
        return s;
    }
}
int main() {
    set<vector<int>> powerset;
    vector<int> given = {1, 2, 3};
    powerset = set<vector<int>>(generate_powerset(given));
    for(set<vector<int>>::iterator iter=powerset.begin(); iter!=powerset.end(); iter++) {
        for(vector<int>::iterator it = ((vector<int>)(*iter)).begin(); it!=(*iter).end(); it++) {
            cout<<(*it)<<endl;
        }
    }
    return 0;
}


