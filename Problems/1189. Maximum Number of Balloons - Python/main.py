class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        dict_letters = {
            'b': 0,
            'a': 0,
            'l': 0,
            'o': 0,
            'n': 0,
        }
        for char in text:
            if char in dict_letters:
                dict_letters[char] += 1
        # print(dict_letters)
        dict_letters['l'] //= 2
        dict_letters['o'] //= 2
        return min(dict_letters.values())


if __name__ == "__main__":
    print('in main')
    # text = "nlaebolko"
    text = "loonbalxballpoon"
    print(Solution().maxNumberOfBalloons(text))