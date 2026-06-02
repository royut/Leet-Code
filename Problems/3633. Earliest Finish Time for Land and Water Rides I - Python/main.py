class Solution(object):
    def earliestFinishTime(self, landStartTime, landDuration, waterStartTime, waterDuration):
        """
        :type landStartTime: List[int]
        :type landDuration: List[int]
        :type waterStartTime: List[int]
        :type waterDuration: List[int]
        :rtype: int
        """
        tempMinFinishTime = float('inf')

        for i in range(len(landStartTime)):
            currentEndTime = landStartTime[i] + landDuration[i]
            for j in range(len(waterStartTime)):
                tempEndTime = currentEndTime
                if waterStartTime[j] > currentEndTime:
                    tempEndTime = waterStartTime[j]
                tempEndTime += waterDuration[j]
                if tempEndTime < tempMinFinishTime:
                    tempMinFinishTime = tempEndTime

        for i in range(len(waterStartTime)):
            currentEndTime = waterStartTime[i] + waterDuration[i]
            for j in range(len(landStartTime)):
                tempEndTime = currentEndTime
                if landStartTime[j] > currentEndTime:
                    tempEndTime = landStartTime[j]
                tempEndTime += landDuration[j]
                if tempEndTime < tempMinFinishTime:
                    tempMinFinishTime = tempEndTime

        return tempMinFinishTime


if __name__ == "__main__":
    print('in main')
    # landStartTime = [2, 8]
    # landDuration = [4, 1]
    # waterStartTime = [6]
    # waterDuration = [3]
    landStartTime = [5]
    landDuration = [3]
    waterStartTime = [1]
    waterDuration = [10]
    print(Solution().earliestFinishTime(landStartTime, landDuration, waterStartTime, waterDuration))