#include <string>
using namespace std;

class Solution {
    public:
        int appendCharacters(string s, string t) {
            int left = 0, right = 0;
            while (left < s.size() and right < t.size()) {
                if (s[left] == t[right]) right++;
                left++;
            }
            return t.size() - right;
        }
};