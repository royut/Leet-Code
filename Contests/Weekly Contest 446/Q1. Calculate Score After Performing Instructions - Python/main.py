class Solution(object):
    def calculateScore(self, instructions, values):
        """
        :type instructions: List[str]
        :type values: List[int]
        :rtype: int
        """
        score = 0
        index = 0
        visited = set()
        while True:
            if index in visited or index >= len(instructions) or index < 0:
                break
            instruction = instructions[index]
            value = values[index]
            if instruction == 'add':
                visited.add(index)
                score += value
                index += 1
            elif instruction == 'jump':
                visited.add(index)
                index += value
        return score


if __name__ == '__main__':
    print('in main')
    # instructions = ["jump", "add", "add", "jump", "add", "jump"]
    # values = [2, 1, 3, 1, -2, -3]
    # instructions = ["jump", "add", "add"]
    # values = [3, 1, 1]
    instructions = ["jump"]
    values = [0]
    print(Solution().calculateScore(instructions, values))