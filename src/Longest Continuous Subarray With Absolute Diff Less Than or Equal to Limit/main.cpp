#include <iostream>
#include <set>
#include <vector>

class Solution {
    public:
        int longestSubarray(std::vector<int>& nums, int limit) {
            std::multiset<int> s;
            int answer = 0, left = 0, right = 0;
            while (left < nums.size() and right < nums.size()) {
                s.insert(nums[right++]);
                while (nums[left] < *s.rbegin() - limit or nums[left] > *s.begin() + limit) s.erase(s.find(nums[left++]));
                answer = std::max((int) s.size(), answer);
            }
            return answer;
        }
};