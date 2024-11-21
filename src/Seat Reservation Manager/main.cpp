#include <set>

class SeatManager {
    std::set<int> s;

    public:
        SeatManager(int n) {
            for (int i = 1; i <= n; ++i) s.insert(i);
        }
        
        int reserve() {
            auto begin = s.begin();
            int temp = *begin;
            s.erase(begin);
            return temp;
        }
        
        void unreserve(int seatNumber) {
            s.insert(seatNumber);
        }
};
