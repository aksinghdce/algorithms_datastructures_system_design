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
