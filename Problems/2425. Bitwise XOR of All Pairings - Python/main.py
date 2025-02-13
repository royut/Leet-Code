class Solution(object):
    def xorAllNums(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        if len(nums2) % 2 == 0:
            XOR = 0
        else:
            XOR = nums1[0]
        for i in range(1,len(nums1)):
            if len(nums2) % 2 == 0:
                XOR = XOR ^ 0
            else:
                XOR = XOR ^ nums1[i]
        for i in range(len(nums2)):
            if len(nums1) % 2 == 0:
                XOR = XOR ^ 0
            else:
                XOR = XOR ^ nums2[i]
        return XOR


if __name__ == '__main__':
    print('in main')
    nums1 = [2, 1, 3]
    nums2 = [10, 2, 5, 0]
    print(Solution().xorAllNums(nums1, nums2))
