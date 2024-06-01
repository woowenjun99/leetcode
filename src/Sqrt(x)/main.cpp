class Solution {
    public:
        int mySqrt(int x) {
            unsigned long long left = 0, right = x;
            while (left <= right) {
                unsigned long long mid = left + (right - left) / 2;
                if (mid * mid == x) return mid;
                if (mid * mid < x) left = mid + 1;
                else right = mid - 1;
            }
            return right;
        }
};