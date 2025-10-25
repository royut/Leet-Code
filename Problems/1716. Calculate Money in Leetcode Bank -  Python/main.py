class Solution(object):
    def totalMoney(self, n):
        """
        :type n: int
        :rtype: int
        """
        base = [0, 1, 3, 6, 10, 15, 21, 28]
        baseCost = 28
        completedWeeks = n // 7
        remainingDays = n % 7
        sumOfWeeks = completedWeeks * (completedWeeks - 1) // 2
        sumWeeksSaving = baseCost * completedWeeks + sumOfWeeks * 7
        sumDaysSaving = remainingDays * completedWeeks + base[remainingDays]
        # print(sumWeeksSaving, sumOfWeeks, completedWeeks)
        # print(sumDaysSaving)
        return sumWeeksSaving + sumDaysSaving


if __name__ == "__main__":
    n = 14
    print(Solution().totalMoney(n))