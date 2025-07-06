class Solution(object):
    def validateCoupons(self, code, businessLine, isActive):
        """
        :type code: List[str]
        :type businessLine: List[str]
        :type isActive: List[bool]
        :rtype: List[str]
        """
        validDicts = []
        for i in range(len(code)):
            if code[i] != '':
                validFlag = True
                for j in code[i]:
                    if not (j.isdigit() or j.isalpha() or j == '_'):
                        validFlag = False
                    if businessLine[i] not in ["electronics", "grocery", "pharmacy", "restaurant"]:
                        validFlag = False
                    if not isActive[i]:
                        validFlag = False
                if validFlag:
                    # v.append(i)
                    validDicts.append({'c': code[i], 'b': businessLine[i]})
        validDicts = sorted(validDicts, key=lambda x: (x['b'], x['c']))
        sortedCodes = []
        for i in range(len(validDicts)):
            sortedCodes.append(validDicts[i]['c'])
        return sortedCodes


if __name__ == '__main__':
    print('in main')
    code = ["SAVE20", "", "PHARMA5", "SAVE@20"]
    businessLine = ["restaurant", "grocery", "pharmacy", "restaurant"]
    isActive = [True, True, True, True]
    Solution().validateCoupons(code, businessLine, isActive)
