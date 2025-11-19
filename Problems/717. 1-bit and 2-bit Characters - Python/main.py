class Solution(object):
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        i = 0
        while i < len(bits):
            if bits[i] == 0:
                if i == len(bits) - 1:
                    return True
                i += 1
            elif bits[i] == 1:
                i += 2
        # print(i)
        return False


if __name__ == '__main__':
    print('in main')
    bits = [1, 0, 0]
    bits = [1, 1, 1, 0]
    print(Solution().isOneBitCharacter(bits))