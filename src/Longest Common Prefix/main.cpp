#include <string>
#include <vector>
using namespace std;

class Solution {
    public:
        string longestCommonPrefix(vector<string>& strs) {
            string answer = strs[0];
            for (int i = 1; i < strs.size(); ++i) {
                int left = 0, right = 0;
                string new_answer = "";
                while (left < answer.size() and right < strs[i].size() and answer[left] == strs[i][right]) {
                    new_answer += answer[left];
                    left++;
                    right++;
                }
                answer = new_answer;
            }
            return answer;
        }
};