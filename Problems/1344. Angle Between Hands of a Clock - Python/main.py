class Solution(object):
    def angleClock(self, hour, minutes):
        """
        :type hour: int
        :type minutes: int
        :rtype: float
        """
        hourDegree = (hour % 12) * (360 / 12)
        hourPastMinutesDegree = 30 * (float(minutes) / 60)
        minutesDegree = minutes * 6
        # print(hourDegree, minutesDegree, hourPastMinutesDegree)
        d = abs(minutesDegree - (hourDegree + hourPastMinutesDegree))
        return min(d, 360-d)


if __name__ == "__main__":
    print('in main')
    hour = 12
    minutes = 30
    print(Solution().angleClock(hour, minutes))