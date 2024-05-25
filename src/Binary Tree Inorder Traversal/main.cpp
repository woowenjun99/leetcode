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
    vector<int> responses;

    void dfs(TreeNode* node) {
        if (not node) return;
        dfs(node->left);
        responses.push_back(node->val);
        dfs(node->right);
    }

    public:
        vector<int> inorderTraversal(TreeNode* root) {
            dfs(root);
            return responses;
        }
};