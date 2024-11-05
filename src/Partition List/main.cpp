#include <queue>

struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
    public:
        ListNode* partition(ListNode* head, int x) {
            std::queue<int> smaller;
            std::queue<int> bigger;
            ListNode* current = head;
            while (current != nullptr) {
                if (current->val < x) smaller.push(current->val);
                else bigger.push(current->val);
                current = current->next;
            }
            ListNode* new_head = new ListNode();
            current = new_head;
            while (smaller.size() > 0) {
                current->next = new ListNode(smaller.front());
                smaller.pop();
                current = current->next;
            }
            while (bigger.size() > 0) {
                current->next = new ListNode(bigger.front());
                bigger.pop();
                current = current->next;
            }
            return new_head->next;
        }
};