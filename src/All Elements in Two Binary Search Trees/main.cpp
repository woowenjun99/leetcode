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
        void dfs(TreeNode* root, std::vector<int>& tree) {
            if (not root) return;
            dfs(root->left, tree);
            tree.push_back(root->val);
            dfs(root->right, tree);
        }

        vector<int> getAllElements(TreeNode* root1, TreeNode* root2) {
            std::vector<int> answer;
            std::vector<int> tree1;
            std::vector<int> tree2;
            dfs(root1, tree1);
            dfs(root2, tree2);
            int left = 0, right = 0;
            while (left < tree1.size() and right < tree2.size()) {
                if (tree1[left] <= tree2[right]) answer.push_back(tree1[left++]);
                else answer.push_back(tree2[right++]);
            }
            while (left < tree1.size()) answer.push_back(tree1[left++]);
            while (right < tree2.size()) answer.push_back(tree2[right++]);
            return answer;
        }
};