class Solution(object):
    def doesValidArrayExist(self, derived):
        """
        :type derived: List[int]
        :rtype: bool
        """
        final = derived[0]
        for i in range(1, len(derived)):
            final ^= derived[i]
        if final == 0:
            return True
        else:
            return False


if __name__ == '__main__':
    print('in main')
    n = [1,1,0]
    print(Solution().doesValidArrayExist(n))