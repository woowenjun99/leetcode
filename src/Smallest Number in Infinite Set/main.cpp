#include <set>

class SmallestInfiniteSet {
    std::set<int> s;

    public:
        SmallestInfiniteSet() {
            for (int i = 1; i <= 1000; ++i) s.insert(i);
        }
        
        int popSmallest() {
            int smallest = *s.begin();
            s.erase(s.find(*s.begin()));
            return smallest;
        }
        
        void addBack(int num) {
            s.insert(num);
        }
};
