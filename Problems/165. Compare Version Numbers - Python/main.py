class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        v1 = version1.split('.')
        v2 = version2.split('.')
        l1 = len(v1)
        l2 = len(v2)
        if l1 != l2:
            if l1 > l2:
                for i in range(l1-l2):
                    v2.append('0')
            else:
                for i in range(l2-l1):
                    v1.append('0')
        for i in range(len(v1)):
            # print(int(v1[i]), int(v2[i]))
            if int(v1[i]) > int(v2[i]):
                return 1
            elif int(v1[i]) < int(v2[i]):
                return -1
        return 0


if __name__ == '__main__':
    print('in main')
    version1 = "1.02"
    version2 = "1.10"
    version1 = "1.01"
    version2 = "1.001"
    version1 = "1.0"
    version2 = "1.0.0.0"
    print(Solution().compareVersion(version1, version2))