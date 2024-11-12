#include <vector>

class Solution {
    public:
        std::vector<int> countBits(int n) {
            std::vector<int> answer(n + 1, 0);
            for (int i = 0; i <= n; ++i) {
                int temp = i;
                while (temp > 0) {
                    answer[i] += temp % 2;
                    temp = temp / 2;
                }
            }
            return answer;
        }
};