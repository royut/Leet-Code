class Solution(object):
    def earliestTime(self, tasks):
        """
        :type tasks: List[List[int]]
        :rtype: int
        """
        minTime = float('inf')
        for i in tasks:
            if i[0] + i[1] < minTime:
                minTime = i[0] + i[1]
        return minTime