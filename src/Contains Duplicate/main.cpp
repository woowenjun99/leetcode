#include <unordered_set>
#include <vector>
using namespace std;

class Solution {
    public:
        bool containsDuplicate(vector<int>& nums) {
            unordered_set<int> appeared;
            for (auto num: nums) {
                if (appeared.find(num) != appeared.end()) return true;
                appeared.insert(num);
            }
            return false;
        }
};