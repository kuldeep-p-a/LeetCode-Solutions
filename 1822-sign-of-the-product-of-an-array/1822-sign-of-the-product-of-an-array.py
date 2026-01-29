class Solution(object):
    def arraySign(self, nums):
        product = 1
        for num in nums:
            product = product*num
        if product == 0:
            return 0
        elif product>0:
            return 1
        elif product<0:
            return -1
obj = Solution()
print(obj.arraySign([-1,-2,-3,-4,3,2,1]))
print(obj.arraySign([1,5,0,2,-3]))
print(obj.arraySign([-1,1,-1,1,-1]))