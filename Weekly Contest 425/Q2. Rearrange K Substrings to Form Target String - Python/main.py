class Solution(object):
    def isPossibleToRearrange(self, s, t, k):
        """
        :type s: str
        :type t: str
        :type k: int
        :rtype: bool
        """
        size = int(len(s) / k)
        t_array = []
        s_array = []
        for i in range(0, len(s), size):
            t_array.append(t[i:i+size])
            s_array.append(s[i:i+size])

        s_array.sort()
        t_array.sort()

        for i in range(len(s_array)):
            if s_array[i] != t_array[i]:
                return False

        return True


if __name__ == '__main__':
    print("in main")
    print(Solution().isPossibleToRearrange('aabbcc', 'bbaacc', 3))
