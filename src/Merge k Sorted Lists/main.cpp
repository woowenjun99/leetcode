#include <algorithm>
#include <vector>
using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
    public:
        ListNode* mergeKLists(vector<ListNode*>& lists) {
            vector<int> nums;
            for (auto l: lists) {
                auto current = l;
                while (current) {
                    nums.push_back(current->val);
                    current = current->next;
                }
            }
            sort(nums.begin(), nums.end());
            ListNode* head = new ListNode();
            ListNode* current = head;
            for (auto num: nums) {
                current->next = new ListNode(num);
                current = current->next;
            }
            return head->next;
        }
};