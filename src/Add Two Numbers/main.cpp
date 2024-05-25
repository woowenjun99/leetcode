struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
    public:
        ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
            ListNode* new_head = new ListNode();
            ListNode* current = new_head;
            int total = 0;
            while (l1 or l2 or total) {
                int l1_val = l1 ? l1->val : 0;
                int l2_val = l2 ? l2->val : 0;
                total += l1_val + l2_val;

                current->next = new ListNode(total % 10);
                current = current->next;
                total /= 10;
                l1 = l1 ? l1->next : nullptr;
                l2 = l2 ? l2->next : nullptr;
            }
            return new_head->next;
        }
};