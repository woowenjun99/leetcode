#include <algorithm>
#include <unordered_map>
#include <string>
using namespace std;

class Solution {
    public:
        int lengthOfLongestSubstringTwoDistinct(string s) {
            std::unordered_map<int, int> mappers;
            int left = 0;
            int answer = 0;
            for (int right = 0; right < s.size(); right++) {
                mappers[s[right]]++;
                int distinct_characters = 0;
                for (auto &[k, v]: mappers) {
                    if (v > 0) distinct_characters++;
                }
                while (distinct_characters > 2) {
                    mappers[s[left]]--;
                    if (mappers[s[left]] == 0) distinct_characters--;
                    left++;
                }
                answer = std::max(answer, right - left + 1);
            }
            return answer;
        }
};