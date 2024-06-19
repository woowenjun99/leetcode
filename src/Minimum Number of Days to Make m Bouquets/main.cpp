#include <iostream>
#include <vector>
using namespace std;

class Solution {
    public:
        int util(std::vector<int> bloomDay, int k, int mid) {
            int count = 0;
            int flowers_made = 0;
            for (auto &day: bloomDay) {
                if (day <= mid) count++;
                else count = 0;
                if (count == k) {
                    flowers_made++;
                    count = 0;
                }
            }
            return flowers_made;
        }
    
        int minDays(vector<int>& bloomDay, int m, int k) {
            if (m * k > bloomDay.size()) return -1;
            int low = *std::min_element(bloomDay.begin(), bloomDay.end());
            int high = *std::max_element(bloomDay.begin(), bloomDay.end());
            int days = -1;
            while (low <= high) {
                int mid = low + (high - low) / 2;
                if (util(bloomDay, k, mid) < m) low = mid + 1;
                else {
                    days = mid;
                    high = mid - 1;
                }
            }
            return days;
        }
};