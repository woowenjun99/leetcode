class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        minute_angle = 6 * minutes
        hour_angle = 30 * (hour % 12) + (minutes / 2)
        return min(abs(minute_angle - hour_angle), 360 - abs(minute_angle - hour_angle))
