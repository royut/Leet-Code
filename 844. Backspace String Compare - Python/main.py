class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: string
        :type t: string
        :rtype: bool
        """
        letter = 0
        i = 0
        while i < len(s):
            if s[i] == '#':
                if letter == 0:
                    s = s[1:]
                else:
                    s = s[:i-1] + s[i+1:]
                    letter -= 1
                    i -= 1
            else:
                i += 1
                letter += 1

        letter = 0
        i = 0
        while i < len(t):
            if t[i] == '#':
                if letter == 0:
                    t = t[1:]
                else:
                    t = t[:i-1] + t[i+1:]
                    letter -= 1
                    i -= 1
            else:
                i += 1
                letter += 1

        return s == t


if __name__ == "__main__":
    print("in main")
    print(Solution().backspaceCompare("y#f#o##f", "asdasd"))
