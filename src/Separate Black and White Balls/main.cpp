#include <string>
using namespace std;

class Solution {
    public:
        long long minimumSteps(string s) {
            long long count = 0, num_of_black = 0;
            for (auto c: s) {
                if (c == '1') num_of_black++;
                else count += num_of_black;
            }
            return count;
        }
};