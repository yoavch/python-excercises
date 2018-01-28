# Given a list, 3 3 numbers that yields the highest
class Max3Multipliers:
    def __init__(self, ls):
        self.lsOfInt = ls
        self.found = []


    def topNumbers(self, minMax, length):
        '''
            Return the smallest / largest numbers from a list based on minMax
            @param minMax: 'min' => return smalles, 'max' => return largest

        '''
        found = []
        def addToFound(e, length, revMaxMinOp):
            # add e to the list, dropping the smallest element if needed to keep the 3 top elements
            nonlocal found
            if len(found) == length:
                rem_e = revMaxMinOp(found)
                found.remove(rem_e)
            found.append(e)

        cmpOp = (lambda x, y: x > y) if minMax == 'max' else (lambda x, y: x < y)
        maxMinOp = (lambda ls : max(ls)) if minMax == 'max' else (lambda ls: min(ls))
        revMaxMinOp = (lambda ls : max(ls)) if minMax == 'min' else (lambda ls: min(ls))
        for e in self.lsOfInt:
            if len(found) < length or cmpOp(e, maxMinOp(found)):
                addToFound(e, length, revMaxMinOp)
        return sorted(found)

    def numPos(self):
        cnt = 0
        for e in self.lsOfInt:
            if e >= 0: cnt += 1
        return cnt

    def numNeg(self):
        return len(self.lsOfInt) - self.numPos()

    def find3Multipliers(self):
        # handled the following cases
        # 1. Less than 3 numbers => enter empty list
        # 2. 3 numbers => return the nubmers
        # 3. 2 or more negative numbers + 1 or 2 positive numbers => find the 2 minmimal negative numbers and multiply
        #       by the largest positive number
        # 4. 2 or more negative numbers + 3 or more positive numbers => find the 2 minimal negative numbers and check
        #       if their multiplication
        #       is larger that the multiplication of the 2nd and 3 highest positive number. Return either the 2
        #       negative number and the highest positive nunmber or the 3 highest positive numbers
        # 5. (1 or 0 negative number + 3 or more positive numbers) or o positive numbers => return the max 3 numbers
        if len(self.lsOfInt) < 3:
            return []
        elif len(self.lsOfInt) == 3:
            return self.lsOfInt
        elif 1 <= self.numPos() <=2  and self.numNeg() >= 2:
            neglist = self.topNumbers('min', 2)
            toplist = self.topNumbers('max', 1)
            return sorted(neglist + toplist)
        elif self.numNeg() >= 2 and self.numPos() >= 3:
            neglist = self.topNumbers('min', 2)
            poslist = self.topNumbers('max', 2)
            if neglist[0] * neglist[1] > poslist[0]:
                return sorted(neglist + neglist[0:1])
        elif (0 <= self.numNeg() <= 1 and self.numPos() >= 3) or self.numPos() == 0:
            return self.topNumbers('max', 3)
        else: print("other option")



tests = [([-2, -1,-2,-3, -12, -13, -41], [-2, -2, -1]),
         ([-1, -2], []),
         ([-9, -8, 1], [-9, -8, 1]),
         ([-9, -8, -13, 9, 1], [-13, -9, 9]),
         ([9, 8, 7, 6, 5], [7, 8, 9]),
         ([-9, -8, -7, 1], [-9, -8, 1])]
# tests = [([-9, -8, -13, 9, 1], [-13, -9, 9])]
for test in tests:
    max3 = Max3Multipliers(test[0])
    list3 = max3.find3Multipliers()
    print (list3, test[1])
    if (list3 != test[1]):
        print('mismatch')
