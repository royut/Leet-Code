class Solution(object):
    def minTime(self, skill, mana):
        """
        :type skill: List[int]
        :type mana: List[int]
        :rtype: int
        """
        m, n = len(mana), len(skill)
        # print(m, n)
        baseTime = [skill[0]]
        for i in range(1, n):
            baseTime.append(baseTime[-1] + skill[i])
        startTimes = [0]
        for i in range(1, m):
            startTime = (baseTime[0] * mana[i-1]) + startTimes[i-1]
            # print(startTime)
            manaSum = 0
            for j in range(n-1):
                manaSum += skill[j] * mana[i]
                if startTime + manaSum < startTimes[-1] + (mana[i-1] * baseTime[j+1]):
                    startTime = startTimes[-1] + (mana[i-1] * baseTime[j+1]) - manaSum
            manaSum += skill[n-1] * mana[i]
            startTimes.append(startTime)
        # print(baseTime, startTimes)
        return startTimes[-1] + (baseTime[-1] * mana[-1])


if __name__ == "__main__":
    skill = [1, 5, 2, 4]
    mana = [5, 1, 4, 2]
    # skill = [1, 1, 1]
    # mana = [1, 1, 1]
    # skill = [1, 2, 3, 4]
    # mana = [1, 2]
    skill = [3,5,3,9]
    mana = [1,10,7,3]
    skill = [5, 4]
    mana = [3, 2, 6, 1]
    print(Solution().minTime(skill, mana))