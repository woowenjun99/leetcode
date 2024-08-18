#include <iostream>
#include <set>
#include <vector>
using namespace std;

class Solution {
    public:
        int maxDistance(vector<vector<int>>& arrays) {
            std::multiset<int> bst;
            for (int i = 1; i < arrays.size(); ++i) {
                bst.insert(arrays[i][0]);
                bst.insert(arrays[i][arrays[i].size() - 1]);
            }

            int answer = 0;
            for (int i = 0; i < arrays.size(); ++i) {
                int bst_min = *bst.begin();
                int bst_max = *bst.rbegin();
                answer = std::max(answer, std::abs(arrays[i][arrays[i].size() - 1] - bst_min));
                answer = std::max(answer, std::abs(bst_max - arrays[i][0]));
                bst.insert(arrays[i][0]);
                bst.insert(arrays[i][arrays[i].size() - 1]);
                if (i < arrays.size() - 1) {
                    bst.erase(bst.find(arrays[i + 1][0]));
                    bst.erase(bst.find(arrays[i + 1][arrays[i + 1].size() - 1]));
                }
            }
            return answer;
        }
};