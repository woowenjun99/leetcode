from typing import List

class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        time_elapsed = total_waiting_time = 0
        for arrival_time, waiting_time in customers:
            time_start = max(arrival_time, time_elapsed)
            time_elapsed = time_start + waiting_time
            total_waiting_time += time_start + waiting_time - arrival_time
        return total_waiting_time / len(customers)