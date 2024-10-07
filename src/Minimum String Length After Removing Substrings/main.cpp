#include <stack>
#include <string>
using namespace std;

class Solution {
    public:
        int minLength(string s) {
            std::stack<char> stack;
            for (auto& c: s) {
                if (c == 'D' and stack.size() and stack.top() == 'C') stack.pop();
                else if (c == 'B' and stack.size() and stack.top() == 'A') stack.pop();
                else stack.push(c);
            }
            return stack.size();
        }
};
