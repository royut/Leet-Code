class Solution(object):
    def sortVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = 'AEIUOaeiou'
        vs = []
        for char in s:
            if char in vowels:
                vs.append(char)
        vs.sort()
        print(vs)
        t = ''
        for char in s:
            if char in vowels:
                t += vs.pop(0)
            else:
                t += char
        return t


if __name__ == "__main__":
    print('in main')
    s = "lEetcOde"
    print(Solution().sortVowels(s))