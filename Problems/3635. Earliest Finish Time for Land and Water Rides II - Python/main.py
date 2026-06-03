class Solution(object):
    def earliestFinishTime(self, landStartTime, landDuration, waterStartTime, waterDuration):
        """
        :type landStartTime: List[int]
        :type landDuration: List[int]
        :type waterStartTime: List[int]
        :type waterDuration: List[int]
        :rtype: int
        """
        minFinishTime = float("inf")
        # land first
        minLandFinishTime = float("inf")
        for i in range(len(landStartTime)):
            if landStartTime[i] + landDuration[i] < minLandFinishTime:
                minLandFinishTime = landStartTime[i] + landDuration[i]
        for i in range(len(waterStartTime)):
            currentFinishTime = minLandFinishTime
            if currentFinishTime < waterStartTime[i]:
                currentFinishTime = waterStartTime[i]
            currentFinishTime += waterDuration[i]
            if currentFinishTime < minFinishTime:
                minFinishTime = currentFinishTime
        # water first
        minWaterFinishTime = float("inf")
        for i in range(len(waterStartTime)):
            if waterStartTime[i] + waterDuration[i] < minWaterFinishTime:
                minWaterFinishTime = waterStartTime[i] + waterDuration[i]
        for i in range(len(landStartTime)):
            currentFinishTime = minWaterFinishTime
            if currentFinishTime < landStartTime[i]:
                currentFinishTime = landStartTime[i]
            currentFinishTime += landDuration[i]
            if currentFinishTime < minFinishTime:
                minFinishTime = currentFinishTime
        return minFinishTime


if __name__ == "__main__":
    print('in main')
    landStartTime = [2, 8]
    landDuration = [7, 1]
    waterStartTime = [6, 3, 9, 11]
    waterDuration = [3, 1, 2, 1]
    print(Solution().earliestFinishTime(landStartTime, landDuration, waterStartTime, waterDuration))
