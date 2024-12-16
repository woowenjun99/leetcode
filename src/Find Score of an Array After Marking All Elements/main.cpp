#include <iostream>
#include <set>
#include <vector>

class Solution {
    public:
        long long findScore(std::vector<int>& nums) {
            long long answer = 0;
            std::set<std::pair<int, int>> available;
            for (int i = 0; i < nums.size(); ++i) available.insert({nums[i], i});

            while (not available.empty()) {
                auto unmarked = available.begin();
                auto [num, index] = *unmarked;
                answer += num;
                available.erase(unmarked);
                if (index - 1 >= 0 and available.find({ nums[index - 1], index - 1 }) != available.end()) {
                    available.erase({ nums[index - 1], index - 1 });
                }
                if (index + 1 < nums.size() and available.find({ nums[index + 1], index + 1 }) != available.end()) {
                    available.erase({ nums[index + 1], index + 1 });
                }
            }
            return answer;
        }
};