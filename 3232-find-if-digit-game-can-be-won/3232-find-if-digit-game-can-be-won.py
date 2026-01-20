class Solution(object):
    def canAliceWin(self, nums):
        sumAl1 = 0
        sumBob1 = 0
        sumAl2 = 0
        sumBob2 = 0
        for item in nums:
            if item >9:
                sumAl1+=item
                sumBob2 +=item
            else:
                sumBob1+=item
                sumAl2+=item
        if sumAl1>sumBob1 or sumAl2>sumBob2:
            return True
        else:
            return False
obj = Solution()
print(obj.canAliceWin([1,2,3,4,10]))
print(obj.canAliceWin([1,2,3,4,5,14]))
print(obj.canAliceWin([5,5,5,25]))
    