#include <algorithm>
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
    std::vector<int> nums;

    void dfs(TreeNode* node) {
        if (not node) return;
        dfs(node->left);
        nums.push_back(node->val);
        dfs(node->right);
    }

    public:
        int getMinimumDifference(TreeNode* root) {
            dfs(root);
            int answer = 1e9;
            for (int i = 1; i < nums.size(); ++i) {
                answer = std::min(answer, nums[i] - nums[i - 1]);
            }
            return answer;
        }
};