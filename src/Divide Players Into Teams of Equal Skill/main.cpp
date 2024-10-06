#include <algorithm>
#include <vector>

class Solution {
    public:
        long long dividePlayers(std::vector<int>& skill) {
            if (skill.size() == 2) return skill[0] * skill[1];
            std::sort(skill.begin(), skill.end());
            long long answer = 0, required = skill[0] + skill[skill.size() - 1];
            int left = 0, right = skill.size() - 1;
            while (left < right) {
                if (skill[left] + skill[right] != required) return -1;
                answer += skill[left++] * skill[right--];
            }
            return answer;
        }
};