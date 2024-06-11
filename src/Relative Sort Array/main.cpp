#include <algorithm>
#include <unordered_map>
#include <vector>
using namespace std;

class Solution {
    public:
        vector<int> relativeSortArray(vector<int>& arr1, vector<int>& arr2) {
            std::unordered_map<int, int> mappers;
            std::vector<int> unused;
            for (auto &num: arr2) mappers[num] = 0;
            for (auto &num: arr1) {
                if (mappers.find(num) == mappers.end()) {
                    unused.push_back(num);
                    continue;
                }
                mappers[num]++;
            }
            std::vector<int> answer;
            for (auto &num: arr2) {
                while (mappers[num] > 0) {
                    answer.push_back(num);
                    mappers[num]--;
                }
            }
            std::sort(unused.begin(), unused.end());
            for (auto &num: unused) answer.push_back(num);
            return answer;
        }
};