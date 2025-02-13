class Solution(object):
    def removeOccurrences(self, s, part):
        """
        :type s: str
        :type part: str
        :rtype: str
        """
        i = 0
        n = len(part)
        while i < len(s) and s != '':
            if s[i:i+n] == part:
                s = s[:i] + s[i + n:]
                i = 0
            else:
                i += 1
        return s


if __name__ == '__main__':
    print('in main')
    s = "kpygkivtlqoockpygkivtlqoocssnextkqzjpycbylkaondsskpygkpygkivtlqoocssnextkqzjpkpygkivtlqoocssnextkqzjpycbylkaondsycbylkaondskivtlqoocssnextkqzjpycbylkaondssnextkqzjpycbylkaondshijzgaovndkjiiuwjtcpdpbkrfsi"
    p = "kpygkivtlqoocssnextkqzjpycbylkaonds"
    # s = "daabcbaabcbc"
    # p = "abc"
    print(Solution().removeOccurrences(s, p))
    s = "kpygkivtlqoockskpygkpygkivtlqoocssnextkqzjpkycbylkaondskivtlqoocssnextkqzjpycbylkaondssnextkqzjpycbylkaondshijzgaovndkjiiuwjtcpdpbkrfsi"