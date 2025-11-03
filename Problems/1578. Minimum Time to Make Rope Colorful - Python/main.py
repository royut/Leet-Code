class Solution(object):
    def minCost(self, colors, neededTime):
        """
        :type colors: str
        :type neededTime: List[int]
        :rtype: int
        """
        flag = 0
        sumMinTime = 0
        for i in range(1, len(colors)):
            if colors[i] == colors[i-1]:
                if not flag:
                    tempSum = neededTime[i-1]
                    tempMax = neededTime[i-1]
                flag = 1
                startIndex = i-1
                tempSum += neededTime[i]
                tempMax = max(tempMax, neededTime[i])
            elif flag:
                # print(startIndex, i, tempSum, tempMax)
                sumMinTime += (tempSum - tempMax)
                flag = 0
        if flag:
            # print(startIndex, len(colors), tempSum, tempMax)
            sumMinTime += (tempSum - tempMax)
        return sumMinTime


if __name__ == '__main__':
    print('in main')
    colors = "abaaccbaa"
    neededTime = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    colors = "abaac"
    neededTime = [1, 2, 3, 4, 5]
    colors = "abc"
    neededTime = [1, 2, 3]
    colors = "aabaa"
    neededTime = [1, 2, 3, 4, 1]
    print(Solution().minCost(colors, neededTime))