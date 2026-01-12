class Solution(object):
    def numIdenticalPairs(self, nums):
        new_nums = nums[:]
        count = 0
        for i in range (0,len(nums)):
            for j in range (0, len(new_nums)):
                if nums[i]==new_nums[j] and i<j:
                    count += 1            
        return count
obj = Solution()
print(obj.numIdenticalPairs([1,2,3,1,1,3]))
print(obj.numIdenticalPairs([1,1,1,1]))
print(obj.numIdenticalPairs([1,2,3]))
print(obj.numIdenticalPairs([1,2,3,1,1,3,1,2,3,1,1,3]))
        