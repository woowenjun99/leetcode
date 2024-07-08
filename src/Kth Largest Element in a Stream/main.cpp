#include <set>
#include <vector>

class KthLargest {
    std::multiset<int> s;
    int k;

    public:
        KthLargest(int k, std::vector<int>& nums) {
            this->k = k;
            for (auto num: nums) s.insert(num);
        }
        
        int add(int val) {
            s.insert(val);
            auto it = s.rbegin();
            for (int i = 0; i < k - 1; ++i) it++;
            return *it;
        }
};