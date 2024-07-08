class Solution {
    public:
        int passThePillow(int n, int time) {
            bool front = true;
            while (time >= n - 1) {
                time -= n - 1;
                front = not front;
            }
            if (front) return 1 + time;
            return n - time;
        }
};