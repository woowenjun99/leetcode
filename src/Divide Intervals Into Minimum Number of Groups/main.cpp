#include <set>
#include <vector>

class Solution {
    public:
        int minGroups(std::vector<std::vector<int>>& intervals) {
            std::multiset<std::pair<int, int>> bst;
            for (int i = 0; i < intervals.size(); ++i) bst.insert({intervals[i][0], intervals[i][1]});
            int answer = 0;
            while (bst.size() != 0) {
                auto it = bst.begin(); // Keep track of the iterator
                while (it != bst.end()) {
                    auto temp = bst.lower_bound({it->second + 1, -1e9});
                    bst.erase(it);
                    it = temp;
                }
                answer += 1;
            }
            return answer;
        }
};
