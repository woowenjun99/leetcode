#include <map>
#include <queue>
#include <vector>
using namespace std;

class Solution {
    public:
        int smallestCommonElement(vector<vector<int>>& mat) {
            std::map<int, std::deque<std::pair<int, int>>> mappers;
            for (int m = 0; m < mat.size(); m++) mappers[mat[m][0]].push_back({m, 0});
            while ((mappers.begin())->second.size() != mat.size()) {
                std::pair<int, int> pair = (mappers.begin())->second.back();
                (mappers.begin())->second.pop_back();
                if ((mappers.begin())->second.empty()) mappers.erase(mappers.begin());
                if (pair.second == mat[0].size() - 1) return -1;
                mappers[mat[pair.first][pair.second + 1]].push_back({pair.first,pair.second + 1});
            }
            return (mappers.begin())->first;
        }
};
