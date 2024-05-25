#include <condition_variable>
#include <mutex>
#include <queue>
using namespace std;

class BoundedBlockingQueue {
    private:
        std::condition_variable condition;
        std::mutex mut;
        std::queue<int> q;
        int capacity;

    public:
        BoundedBlockingQueue(int capacity) {
            this->capacity = capacity;
        }
            
        void enqueue(int element) {
            std::unique_lock lock{mut};
            condition.wait(lock, [this] { return q.size() < capacity; });
            q.push(element);
            lock.unlock();
            condition.notify_one();
        }
            
        int dequeue() {
            std::unique_lock lock{mut};
            condition.wait(lock, [this] { return q.size() > 0; });
            int front = q.front();
            q.pop();
            lock.unlock();
            condition.notify_one();
            return front;
        }
        
        int size() {
            std::lock_guard lock{mut};
            return q.size();
        }
};