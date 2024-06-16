#include <vector>
using namespace std;

class Solution {
    public:
        int countCompleteDayPairs(vector<int>& hours) {
            int answer = 0;
            std::vector<int> cache(24, 0);
            for (int i = 0; i < hours.size(); ++i) {
                answer += cache[(24 - (hours[i] % 24)) % 24];
                cache[hours[i] % 24] += 1;
            }
            return answer;
        }
};