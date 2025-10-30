class Solution(object):
    def minNumberOperations(self, gate):
        ops = gate[0]
        for i in range(1, len(gate)):
            diff = gate[i] - gate[i - 1]
            if diff > 0:
                ops += diff
        return ops


if __name__ == "__main__":
    print("in main")
    target = [2, 1, 2, 3, 2, 1, 2, 1, 3]
    # target = [3, 1, 1, 2]
    # target = [1, 1, 1, 1, 1212313131]
    # print(Solution().minNumberOperations(target))
    print(Solution().minNumOps(target))