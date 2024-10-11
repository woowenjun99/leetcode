#include <algorithm>
#include <vector>
using namespace std;

class Solution {
    public:
        int maxNumberOfApples(vector<int>& weight) {
            std::sort(weight.begin(), weight.end());
            int count = 0;
            int total = 0;
            for (; count < weight.size(); ++count) {
                if (total + weight[count] > 5000) break;
                total += weight[count];
            }
            return count;
        }
};