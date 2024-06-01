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
        bool dfs(TreeNode* root, int targetSum, int currentSum) {
            if (not root) return false;
            if (not root->left and not root->right and (currentSum + root->val == targetSum)) return true;
            return dfs(root->left, targetSum, currentSum + root->val) or dfs(root->right, targetSum, currentSum + root->val);
        }

        bool hasPathSum(TreeNode* root, int targetSum) { return dfs(root, targetSum, 0); }
};