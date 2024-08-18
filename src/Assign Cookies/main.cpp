#include <algorithm>
#include <vector>
using namespace std;

class Solution {
    public:
        int findContentChildren(vector<int>& g, vector<int>& s) {
            std::sort(g.begin(), g.end());
            std::sort(s.begin(), s.end());
            int left = 0, right = 0;
            while (left < g.size() and right < s.size()) {
                if (s[right] >= g[left]) left++;
                right++;
            }
            return left;
        }
};
