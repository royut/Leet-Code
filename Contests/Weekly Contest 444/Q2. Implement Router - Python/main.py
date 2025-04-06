class Router(object):

    def __init__(self, memoryLimit):
        """
        :type memoryLimit: int
        """
        self.memoryLimit = memoryLimit
        self.packets = []
        self.timeStamps = {}

    def addPacket(self, source, destination, timestamp):
        """
        :type source: int
        :type destination: int
        :type timestamp: int
        :rtype: bool
        """
        for packet in self.packets:
            if packet[0] == source and packet[1] == destination and packet[2] == timestamp:
                return False

        if len(self.packets) >= self.memoryLimit:
            self.packets.pop(0)

        self.packets.append([source, destination, timestamp])
        return True

    def forwardPacket(self):
        """
        :rtype: List[int]
        """
        if len(self.packets) > 0:
            return self.packets.pop(0)
        return []

    def getCount(self, destination, startTime, endTime):
        """
        :type destination: int
        :type startTime: int
        :type endTime: int
        :rtype: int
        """
        if len(self.packets) == 0:
            return 0
        countPackets = 0
        # print(self.packets, startTime, endTime)
        left, right = 0, len(self.packets) - 1
        if startTime <= self.packets[0][2]:
            startIndex = 0
        elif startTime >= self.packets[-1][2]:
            startIndex = len(self.packets) - 1
        else:
            while True:
                mid = (left + right) // 2
                if self.packets[mid][2] <= startTime and self.packets[mid+1][2] >= startTime:
                    startIndex = mid
                    break
                elif self.packets[mid][2] > startTime:
                    right = mid
                elif self.packets[mid][2] < startTime:
                    left = mid
        left, right = startIndex, len(self.packets) - 1
        endTime += 1
        if endTime <= self.packets[0][2]:
            endIndex = 0
        elif endTime >= self.packets[-1][2]:
            endIndex = len(self.packets) - 1
        else:
            while True:
                mid = (left + right) // 2
                if self.packets[mid][2] <= endTime and self.packets[mid+1][2] >= endTime:
                    endIndex = mid
                    break
                elif self.packets[mid][2] > endTime:
                    right = mid
                elif self.packets[mid][2] < endTime:
                    left = mid

        # print('start and end', startIndex, endIndex)
        # print(self.packets[startIndex:endIndex+1])
        endTime -= 1
        for packet in self.packets[startIndex:endIndex+1]:
            if packet[1] == destination and startTime <= packet[2] <= endTime:
                countPackets += 1
        return countPackets

# Your Router object will be instantiated and called as such:
# obj = Router(memoryLimit)
# param_1 = obj.addPacket(source,destination,timestamp)
# param_2 = obj.forwardPacket()
# param_3 = obj.getCount(destination,startTime,endTime)


if __name__ == '__main__':
    print('in main')
    router = Router(3)  # Initialize Router with memoryLimit of 3.
    print(router.addPacket(1, 4, 90))  # Packet is added. Return True.
    print(router.addPacket(2, 5, 90))  # Packet is added. Return True.
    print(router.addPacket(1, 4, 90))  # This is a duplicate packet. Return False.
    print(router.addPacket(3, 5, 95))  # Packet is added. Return True
    print(router.addPacket(4, 5, 105))  # Packet is added, [1, 4, 90] is removed as number of packets exceeds memoryLimit. Return True.
    print(router.forwardPacket())  # Return [2, 5, 90] and remove it from router.
    print(router.addPacket(5, 2, 110))  # Packet is added. Return True.
    print(router.getCount(5, 100, 110))  # The only packet with destination 5 and timestamp in the inclusive range [100, 110] is [4, 5, 105]. Return 1.©leetcode