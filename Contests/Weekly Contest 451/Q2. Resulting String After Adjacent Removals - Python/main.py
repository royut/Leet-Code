class Solution(object):
    def resultingString(self, s):
        """
        :type s: str
        :rtype: str
        """
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        index = 1
        s = list(s)
        # print(s)
        consecutiveFlag = False
        while True:
            print(index)
            if len(s) == 0 or len(s) == 1:
                break
            c1 = alphabet.find(s[index-1])
            c2 = alphabet.find(s[index])
            print(c1, s[index-1], c2, s[index])
            if abs(c1 - c2) == 1 or (c1 == 0 and c2 == 25) or (c1 == 25 and c2 == 0):
                consecutiveFlag = True
                s.pop(index-1)
                s.pop(index-1)
                print('consecutiveFlag', s)
                # index -= 2
            else:
                index += 1
            if index >= len(s):
                print(index, consecutiveFlag)
                if not consecutiveFlag:
                    break
                else:
                    index = 1
                    consecutiveFlag = False
        string = ''
        for char in s:
            string += char
        return string


if __name__ == '__main__':
    print('in main')
    print(Solution().resultingString('llgjfiiil'))