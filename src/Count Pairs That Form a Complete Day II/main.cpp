#include <vector>
using namespace std;

class Solution {
    public:
        long long countCompleteDayPairs(vector<int>& hours) {
            long long answer = 0;
            std::vector<long long> cache(24, 0);
            for (int i = 0; i < hours.size(); ++i) {
                answer += cache[(24 - (hours[i] % 24)) % 24];
                cache[hours[i] % 24] += 1;
            }
            return answer;
        }
};