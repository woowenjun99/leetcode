#include <functional>
#include <mutex>
using namespace std;

class FooBar {
    private:
        int n;
        std::mutex odd_mut;
        std::mutex even_mut;

    public:
        FooBar(int n) {
            this->n = n;
            even_mut.lock();
        }

        void foo(function<void()> printFoo) {
            for (int i = 0; i < n; i++) {
                odd_mut.lock();
                printFoo();
                even_mut.unlock();
            }
        }

        void bar(function<void()> printBar) {
            for (int i = 0; i < n; i++) {
                even_mut.lock();
                printBar();
                odd_mut.unlock();
            }
        }
};