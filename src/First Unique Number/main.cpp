#include <map>
#include <unordered_map>
#include <vector>

class FirstUnique {
    int index = 0;
    std::map<int, int> queue;
    std::unordered_map<int, int> counter;
    std::unordered_map<int, int> mappers;

    public:
        FirstUnique(std::vector<int>& nums) {
            for (auto num: nums) counter[num]++;
            
            for (auto num: nums) {
                if (counter[num] >= 2) continue;
                queue[index] = num;
                mappers[num] = index;
                index++;
            }
        }
        
        int showFirstUnique() {
            if (not queue.size()) return -1;
            return queue.begin()->second;
        }
        
        void add(int value) {
            counter[value]++;
            if (counter[value] == 1) {
                queue[index] = value;
                mappers[value] = index;
                index++;
                return;
            }

            if (counter[value] == 2) {
                queue.erase(mappers[value]);
                mappers.erase(value);
            }
        }
};
