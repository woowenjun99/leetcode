#include <unordered_map>
#include <vector>
using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution {
    public:
        void dfs(TreeNode* root, std::unordered_map<int, int>& counter) {
            if (not root) return;
            dfs(root->left, counter);
            counter[root->val]++;
            dfs(root->right, counter);
        }

        vector<int> findMode(TreeNode* root) {
            std::unordered_map<int, int> counter;
            dfs(root, counter);
            std::vector<int> answer;
            int mode = 0;
            for (auto &[k, v]: counter) if (v > mode) mode = v;
            for (auto &[k, v]: counter) if (v == mode) answer.push_back(k);
            return answer;
        }
};