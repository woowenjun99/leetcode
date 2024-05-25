#include <unordered_map>
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
        ListNode* deleteDuplicates(ListNode* head) {
            unordered_map<int, int> counter;
            vector<int> numbers;
            while (head) {
                if (numbers.empty() or numbers[numbers.size() - 1] != head->val) numbers.push_back(head->val);
                counter[head->val]++;
                head = head->next;
            }

            ListNode* new_head = new ListNode();
            ListNode* current = new_head;
            for (auto num: numbers) {
                if (counter[num] >= 2) continue;
                current->next = new ListNode(num);
                current = current->next; 
            }
            return new_head->next;
        }
};