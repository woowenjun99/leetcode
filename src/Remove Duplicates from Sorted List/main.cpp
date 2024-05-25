#include <queue>
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
    ListNode* deleteDuplicates(ListNode* head) {
        deque<int> dq;
        ListNode* current = head;
        while (current) {
            if (dq.empty() or dq.back() != current->val) dq.push_back(current->val);
            current = current->next;
        }
        ListNode* new_head = new ListNode();
        current = new_head;
        while (not dq.empty()) {
            current->next = new ListNode(dq.front());
            current = current->next;
            dq.pop_front();
        }
        return new_head->next;
    }
};