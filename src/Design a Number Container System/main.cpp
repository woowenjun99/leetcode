#include <set>
#include <unordered_map>

class NumberContainers {
    std::unordered_map<int, std::set<int>> number_to_indexes; // Store number to indexes
    std::unordered_map<int, int> index_to_number; // Store index to number

    public:        
        void change(int index, int number) {
            if (index_to_number.find(index) != index_to_number.end()) {
                int old_num = index_to_number[index];
                number_to_indexes[old_num].erase(index);
            }
            index_to_number[index] = number;
            number_to_indexes[number].insert(index);
        }
        
        int find(int number) {
            if (number_to_indexes.find(number) == number_to_indexes.end() or number_to_indexes[number].empty()) return -1;
            return *number_to_indexes[number].begin();
        }
};
