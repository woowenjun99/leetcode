#include <unordered_map>
#include <vector>
using namespace std;

class Solution {
    public:
        vector<int> twoSum(vector<int>& nums, int target) {
            vector<int> answer(2);
            unordered_map<int, int> mappers;
            for (int i = 0; i < nums.size(); ++i) {
                if (mappers.find(nums[i]) != mappers.end()) {
                    answer[0] = mappers[nums[i]];
                    answer[1] = i;
                    break;
                }
                mappers[target - nums[i]] = i;
            }
            return answer;
        }
};