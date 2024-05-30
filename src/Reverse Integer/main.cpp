#include <queue> 

class Solution {
    public:
        int reverse(int x) {
            if (x == 0) return 0;

            bool is_negative = x < 0;
            int absolute_of_x = std::abs(x);
            std::queue<int> q;
            while (absolute_of_x > 0) {
                q.push(absolute_of_x % 10);
                absolute_of_x /= 10;
            }

            int base = 0;
            int before_limit = is_negative ? -214748364 : 214748364;
            while (q.size() > 1) {
                base = base * 10 + (is_negative ? -q.front() : q.front());
                q.pop();
            }


            if ((is_negative and base < before_limit) or (not is_negative and base > before_limit)) return 0;
            if (base == before_limit) {
                if (is_negative and q.front() == 7) return 0;
                if (not is_negative and q.front() >= 8) return 0;
            }

            return base * 10 + (is_negative ? -q.front() : q.front());
        }
};