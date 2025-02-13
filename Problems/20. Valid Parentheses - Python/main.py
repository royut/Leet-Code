class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for char in s:
            if char in ['(', '{', '[']:
                stack.append(char)
            elif len(stack) != 0:
                if char == ')' and stack[-1] == '(':
                    stack.pop()
                elif char == ']' and stack[-1] == '[':
                    stack.pop()
                elif char == '}' and stack[-1] == '{':
                    stack.pop()
                else:
                    return False
            else:
                return False
        return len(stack) == 0


if __name__ == '__main__':
    print('in main')
    s = "(])"
    print(Solution().isValid(s))