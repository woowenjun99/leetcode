#include <iostream>
#include <unordered_map>
#include <vector>
using namespace std;

class Solution {
    public:
        int numberOfSubarrays(vector<int>& nums, int k) {
            int answer = 0;
            int current_sum = 0;
            std::unordered_map<int, int> mappers;
            mappers[0] = 1;
            for (int i = 0; i < nums.size(); ++i) {
                current_sum += nums[i] % 2;
                answer += mappers[current_sum - k];
                mappers[current_sum]++;
            }
            return answer;
        }
};