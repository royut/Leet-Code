class Solution(object):
    def numberOfBeams(self, bank):
        """
        :type bank: List[str]
        :rtype: int
        """
        lastOccupiedRow = 0
        beams = 0
        for row in bank:
            current = row.count("1")
            if current != 0:
                beams += current * lastOccupiedRow
                lastOccupiedRow = current
        return beams


if __name__ == "__main__":
    bank = ["011001", "000000", "010100", "001000"]
    bank = ["000", "111", "000"]
    bank = ["001", "000", "100"]
    print(Solution().numberOfBeams(bank))