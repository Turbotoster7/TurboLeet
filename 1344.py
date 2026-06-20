# 1 minuta to 6 stopni
class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        angle_hour = (hour%12 * 30) + (minutes * 0.5)
        angle_minute = minutes * 6
        diff = abs(angle_hour - angle_minute)
        return min(diff, 360 - diff)

s = Solution()
hour = 3
minutes = 30
print(s.angleClock(hour, minutes))