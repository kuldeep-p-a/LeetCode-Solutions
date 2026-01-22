class Solution(object):
    def findNumbers(self, nums):
        count = 0
        for item in nums:
            item_str = str(item)
            if len(item_str)%2==0:
                count += 1
        return count
obj = Solution()
print(obj.findNumbers([12,345,2,6,7896]))
print(obj.findNumbers([555,901,482,1771]))