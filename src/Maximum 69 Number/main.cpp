#include <vector>

class Solution {
public:
    int maximum69Number (int num) {
        std::vector<int> stack;
        while (num > 0) {
            stack.push_back(num % 10);
            num /= 10;
        }

        for (int i = stack.size() - 1; i >= 0; --i) {
            if (stack[i] == 9) continue;
            stack[i] = 9;
            break;
        }

        num = 0;
        for (int i = stack.size() - 1; i >= 0; --i) num = num * 10 + stack[i];
        return num;
    }
};