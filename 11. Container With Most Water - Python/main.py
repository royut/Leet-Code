class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxArea = 0
        left, right = 0, len(height) - 1
        while left < right:
            tempArea = min(height[left], height[right]) * (right - left)
            if tempArea > maxArea:
                maxArea = tempArea
            if height[right] < height[left]:
                right -= 1
            else:
                left += 1
        return maxArea


if __name__ == '__main__':
    print('in main')
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    height = [1, 2, 1]
    height = [1, 8, 6, 2, 5, 4, 8, 25, 7]
    print(Solution().maxArea(height))