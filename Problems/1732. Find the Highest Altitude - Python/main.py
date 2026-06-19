class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        curr = 0
        maxSoFar = 0
        for g in gain:
            curr += g
            if curr > maxSoFar:
                maxSoFar = curr
        return maxSoFar