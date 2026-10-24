class Solution(object):
    def countDaysTogether(self, arriveAlice, leaveAlice, arriveBob, leaveBob):
        """
        :type arriveAlice: str
        :type leaveAlice: str
        :type arriveBob: str
        :type leaveBob: str
        :rtype: int
        """
        months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        alice_arrive_day = sum(months[:int(arriveAlice[:2])-1]) + int(arriveAlice[3:])
        alice_leave_day = sum(months[:int(leaveAlice[:2])-1]) + int(leaveAlice[3:])
        bob_arrive_day = sum(months[:int(arriveBob[:2])-1]) + int(arriveBob[3:])
        bob_leave_day = sum(months[:int(leaveBob[:2])-1]) + int(leaveBob[3:])
        count_days = 0
        count_days_together = 0
        for month in range(1, len(months)+1):
            for day in range(1, months[month-1]+1):
                count_days += 1
                if alice_arrive_day <= count_days <= alice_leave_day and bob_arrive_day <= count_days <= bob_leave_day:
                    count_days_together += 1
        # print(count_days, count_days_together)
        return count_days_together


if __name__ == "__main__":
    print('in main')
    arriveAlice = "08-15"
    leaveAlice = "08-18"
    arriveBob = "08-16"
    leaveBob = "08-19"
    print(Solution().countDaysTogether(arriveAlice, leaveAlice, arriveBob, leaveBob))