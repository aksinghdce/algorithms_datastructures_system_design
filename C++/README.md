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

# Using unique_ptr for implementing a Linked List based algorithm to add large integers

Here's the algorithm:

```

#include <iostream>
#include <memory>
using namespace std;

struct ListNode {
    int val;
    unique_ptr<ListNode> next;
    ListNode(int x) : val(x), next(nullptr) {}
};

class Solution {
public:
    unique_ptr<ListNode> addTwoNumbers(unique_ptr<ListNode> l1, unique_ptr<ListNode> l2) {
        ListNode* result=nullptr;
        int carry= 0;
        int count = 0;
        ListNode* p1 = l1.get();
        ListNode* p2 = l2.get();
        ListNode* pr = nullptr;
        while(p1 != nullptr && p2 != nullptr) {
            cout << "val1:" << p1->val << ",val2:" << p2->val << endl; 
            int sum = carry + p1->val + p2->val;
            carry = sum / 10;
            sum = sum % 10;
            cout << "sum:" << sum << ",carry:" << carry << endl;
            if(! result) {
                result = new ListNode(sum);
                count += 1;
                pr = result;
            } else {
                pr->next = unique_ptr<ListNode> (new ListNode(sum));
                count += 1;
                pr = (pr->next).get();
            }
            p1 = p1->next.get();
            p2 = p2->next.get();
        }
        ListNode* p = p1?p1:p2;
        if(p == nullptr && carry > 0) {//both pointers are null here
            pr->next = unique_ptr<ListNode> (new ListNode(carry));
            count += 1;
            carry = 0;
            pr = pr->next.get();
        }else{
            while(p != nullptr) {
                cout << "val:" << p->val << ",carry:" << carry << endl; 
                int sum = carry + p->val;
                carry = sum / 10;
                sum = sum % 10;
                cout << "sum:" << sum << ",carry:" << carry << endl;
                pr->next = unique_ptr<ListNode> (new ListNode(sum));
                pr = pr->next.get();
                count += 1;
                p = p->next.get();
            }
            if(carry > 0) {
                cout << "carry:" << carry << endl; 
                pr->next = unique_ptr<ListNode>(new ListNode(carry));
                pr = pr->next.get();
                count += 1;
                carry = 0;
                pr = pr->next.get();
            }
        }
        cout << "number of nodes created:" << count << endl;
        ListNode* iter = result;
        while(iter != nullptr) {
            cout << "->" << iter->val;
            iter = iter->next.get();
        }
        cout << endl;
        return unique_ptr<ListNode>(result);
    }
};

int main() {
    Solution sol = Solution();
    ListNode* l1 = new ListNode(1);
    ListNode* l2 = new ListNode(9);
    l2->next = unique_ptr<ListNode>(new ListNode(9));
    unique_ptr<ListNode> result = sol.addTwoNumbers(
        unique_ptr<ListNode> (l1), 
        unique_ptr<ListNode> (l2)
        );
    if(result == nullptr) {
        cout<<"Result is a nullptr"<<endl;
    } else {
        ListNode* p = result.get();
        while(p!=nullptr) {
            cout<<p->val<<endl;
            p = p->next.get();
        }
    }
}

```

Here I learnt that in order to iterate over a linked list we need to use plain old pointer. This is because unique_ptr, shared_ptr and weak_ptr take ownership of the pointed-to object.

I explored the question on [reddit](https://www.reddit.com/r/cpp/comments/bwg2we/which_of_these_c17_pointers_should_i_use_for/) and found out that the "correct way to deal with this is to create an iterator type that doesn't own the data structure". So, to find out how to implement an iterator type so that it doesn't own the data structure I need to dig deeper.
    
Another [response in reddit](https://www.reddit.com/r/cpp/comments/bwg2we/which_of_these_c17_pointers_should_i_use_for/epy5v0b/) explains in very helpful detail about how to go about implementing a container in C++. I want to do this exercise to get a bigger grasp on C++ language fundamentals and become a programming language geek :)

Another response shared a video. This video talks about leak-free coding with C++. Here is [a slide](https://youtu.be/JfmTagWcqoE?t=309) that explains three strategies.

Use Pimpl for reducing compile-time dependency. This [portion of video](https://youtu.be/JfmTagWcqoE?t=660) suggests to use const unique_ptr<T>.
    
[Example of a Tree](https://youtu.be/JfmTagWcqoE?t=882) with unique_ptr<T>
    
Tree of unique_ptr<T> has a problem of [recursive deallocation and limited stack space](https://youtu.be/JfmTagWcqoE?t=1096).

How to make a [doubly-linked list](https://youtu.be/JfmTagWcqoE?t=1470)

[shared-ptr](https://youtu.be/JfmTagWcqoE?t=1757) begins and I have so many doubts about shared_ptr aliasing constructor.

Interesting code about [Factory + Cache](https://youtu.be/JfmTagWcqoE?t=2035)

Need to re-watch this video and begin writing amazing C++ code. And, apparently [writing code by using STL](https://youtu.be/JfmTagWcqoE?t=3134) is considered best practice.

