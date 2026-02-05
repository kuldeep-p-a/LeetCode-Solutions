class Solution(object):
    def sortedSquares(self, nums):
        sqr_array = []
        for item in nums:
            sqr_array.append(item**2)
        sqr_array.sort()
        return sqr_array
obj = Solution()
print(obj.sortedSquares([-4,-1,0,3,10]))
print(obj.sortedSquares([-7,-3,2,3,11]))