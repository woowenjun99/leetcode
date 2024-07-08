class Solution {
    public:
        int numWaterBottles(int numBottles, int numExchange) {
            int answer = 0;
            while (numBottles >= numExchange) {
                int bottles_exchanged = numBottles / numExchange;
                int bottles_drank = bottles_exchanged * numExchange;
                answer += bottles_drank;
                numBottles = numBottles - bottles_drank + bottles_exchanged;
            }
            return answer + numBottles;
        }
};