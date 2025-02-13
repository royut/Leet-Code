class Solution(object):
    def stringMatching(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        subs = []
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if words[i] in words[j]:
                    subs.append(words[i])
                if words[j] in words[i]:
                    subs.append(words[j])
        return list(set(subs))


if __name__ == '__main__':
    print('in main')
    words = ["mass","as","hero","superhero"]
    print(Solution().stringMatching(words))