#include <string>
#include <unordered_set>
#include <queue>
using namespace std;

class Solution {
    public:
        int lengthOfLongestSubstring(string s) {
            unordered_set<char> used;
            int max_length = 0;
            deque<char> dq;
            for (auto c: s) {
                while (not dq.empty() and used.find(c) != used.end()) {
                    used.erase(dq.front());
                    dq.pop_front();
                }
                dq.push_back(c);
                used.insert(c);
                max_length = max(max_length, (int) dq.size());
            }
            return max_length;
        }
};