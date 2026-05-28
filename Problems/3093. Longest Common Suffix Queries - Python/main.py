class TrieNode:
    def __init__(self):
        self.children = {}
        self.min_len = float("inf")
        self.index = float("inf")


class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.endChar = "*"

    def add(self, word, index):
        currentNode = self.root
        if len(word) < currentNode.min_len:
            currentNode.min_len = len(word)
            currentNode.index = index
        for char in word:
            if char not in currentNode.children:
                currentNode.children[char] = TrieNode()
            currentNode = currentNode.children[char]
            if len(word) < currentNode.min_len:
                currentNode.min_len = len(word)
                currentNode.index = index
        currentNode.children[self.endChar] = True

    def longestPrefix(self, word):
        currentNode = self.root
        for char in word:
            if char not in currentNode.children:
                break
            currentNode = currentNode.children[char]
        return currentNode.index


class Solution(object):
    def stringIndices(self, wordsContainer, wordsQuery):
        """
        :type wordsContainer: List[str]
        :type wordsQuery: List[str]
        :rtype: List[int]
        """
        for i in range(len(wordsContainer)):
            wordsContainer[i] = wordsContainer[i][::-1]
        for i in range(len(wordsQuery)):
            wordsQuery[i] = wordsQuery[i][::-1]
        # print(wordsContainer, wordsQuery)
        trie = Trie()
        for i in range(len(wordsContainer)):
            trie.add(wordsContainer[i], i)
        ans = []
        for i in range(len(wordsQuery)):
            ans.append(trie.longestPrefix(wordsQuery[i]))
        return ans


if __name__ == "__main__":
    print('in main')
    # wordsContainer = ["abcd", "bcd", "xbcd"]
    # wordsQuery = ["cd", "bcd", "xyz"]
    wordsContainer = ["abcdefgh", "poiuygh", "ghghgh"]
    wordsQuery = ["gh", "acbfgh", "acbfegh"]
    print(Solution().stringIndices(wordsContainer, wordsQuery))