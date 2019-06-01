# C++ On JetBrains CLion

```
#include <iostream>
#include <string>
#include <climits>
#include <vector>
using namespace std;

int main() {
    //cout << "Hello, World!" << endl;
    //cout << "Please Enter a String" << endl;
    //string string1;
    //cout << "Please enter a line" << endl;
    //getline(cin, string1);
    //cout << "The line:" << string1 << endl;
    cout << "Bits in a char:" << CHAR_BIT << endl;
    cout << "Size of a char:" << sizeof(char) << endl;
    cout << "Size of an int:" << sizeof(int) << endl;
    cout << "Size of float:" << sizeof(float) << endl;
    cout << "Size of double:" << sizeof(double) << endl;
    cout << "Size of long:" << sizeof(long) << endl;
    cout << "Size of long long:" << sizeof(long long) << endl;
    cout << "Size of long double:" << sizeof(long double) << endl;
    vector<string> names;
    string name;
    cout << "Enter names:\n";
    while(cin >> name) {
        if(name == "Done") {
            break;
        }
        names.push_back(name);
    }
    for(auto & n:names) {
        cout << n + ",";
    }
    cout << endl;
    return 0;
}
```

# Create powerset of a vector<int>
    
```
#include <iostream>
#include <vector>
#include <cassert>

using namespace std;

class Superset {
private:
    vector<vector<int>> S;
    vector<int> init;
    void generate_set(vector<int> &v, int index) {
        if(index == init.size()){
            S.push_back(v);
            return;
        }
        else {
            v.push_back(init[index]);
            generate_set(v, index+1);
            v.pop_back();
            generate_set(v, index+1);
        }
    }
public:
    explicit Superset(const vector<int>& in) {
        if(! in.empty()) {
            init = in;
        }
    }
    vector<vector<int>> get_supersets() {
        vector<int> v;
        generate_set(v, 0);
        return S;
    }
    friend ostream& operator<<(ostream &o, Superset& sup) {
        for(auto & i: sup.S) {
           for(auto & ii:i) {
               o << ii;
           }
           o << endl;
        }
        return o;
    }
};

int main() {
    vector<int> v = {1, 2, 3, 4, 5, 6, 7, 8};
    Superset s = Superset(v);
    vector<vector<int>> supersets = s.get_supersets();
    cout << "Superset:" << s;
    short size_s = supersets.size();
    short v_size = v.size();
    assert((1<<v_size) == size_s);
    return 0;
}
```
    
Question: Does vector<int>::push_back(int x) pushes a copy of x in the vector?
    
Answer: vector<T>.push_back(T& x) and vector<T>.push_back(T&& x) are two variants of push_back. The first one is copying x into the vector push_back is called on and second one is moving x. For moving the syntax is V.push_back(std::move(x));
    
    
