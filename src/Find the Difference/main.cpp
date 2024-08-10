#include <string>
#include <vector>
using namespace std;

class Solution {
    public:
        char findTheDifference(string s, string t) {
            std::vector<int> count(26, 0);
            for (auto c: s) count[c - 'a']++;
            for (auto c: t) count[c - 'a']--;
            int index = 0;
            while (not count[index]) index++;
            return 'a' + index;
        }
};