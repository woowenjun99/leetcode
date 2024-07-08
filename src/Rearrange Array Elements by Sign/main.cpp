#include <queue>
#include <vector>
using namespace std;

class Solution {
    public:
        vector<int> rearrangeArray(vector<int>& nums) {
            std::deque<int> positives;
            std::deque<int> negatives;
            for (auto num: nums) {
                if (num < 0) negatives.push_back(num);
                else positives.push_back(num);
            }

            std::vector<int> answer;
            while (not positives.empty() and not negatives.empty()) {
                answer.push_back(positives.front());
                positives.pop_front();
                answer.push_back(negatives.front());
                negatives.pop_front();
            }
            return answer;
        }
};