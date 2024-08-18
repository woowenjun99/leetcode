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
        TreeNode* searchBST(TreeNode* root, int val) {
            TreeNode* answer = root;
            while (answer != nullptr and answer->val != val) {
                if (answer->val < val) answer = answer->right;
                else answer = answer->left;
            }
            return answer;
        }
};