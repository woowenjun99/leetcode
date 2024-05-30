#include <queue>
#include <unordered_map>
#include <unordered_set>
#include <vector>

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
        void dfs(TreeNode* root, std::unordered_map<int, std::vector<int>>& graph) {
            if (not root) return;
            if (root->left) {
                graph[root->val].push_back(root->left->val);
                graph[root->left->val].push_back(root->val);
                dfs(root->left, graph);
            }
            if (root->right) {
                graph[root->val].push_back(root->right->val);
                graph[root->right->val].push_back(root->val);
                dfs(root->right, graph);         
            }
        }

        int bfs(int start, std::unordered_map<int, std::vector<int>>& graph) {
            std::queue<std::pair<int, int>> q;
            q.push({start, 0});
            int time_taken = -1;
            std::unordered_set<int> visited;
            visited.insert(start);
            while (not q.empty()) {
                auto [front, time_of_infection] = q.front();
                q.pop();
                time_taken = std::max(time_of_infection, time_taken);
                for (auto neighbour: graph[front]) {
                    if (visited.find(neighbour) == visited.end()) {
                        visited.insert(neighbour);
                        q.push({neighbour, time_of_infection + 1});
                    }
                }
            }
            return time_taken;
        }

        int amountOfTime(TreeNode* root, int start) {
            std::unordered_map<int, std::vector<int>> graph;
            dfs(root, graph);
            return bfs(start, graph);
        }
};