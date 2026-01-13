class Solution(object):
    def triangleType(self, nums):
        for i in range(0,3):
            if nums[i]+nums[i+1]<=nums[i+2] or nums[i+1]+nums[i+2]<=nums[0] or nums[i+2]+nums[i]<=nums[i+1]:
                return "none"
            else:
                if nums[i]==nums[i+1]==nums[i+2]:
                    return "equilateral"
                elif nums[i]==nums[i+1] or nums[i+1]==nums[i+2] or nums[i+2]==nums[i]:
                    return "isosceles"
                else:
                    return "scalene"
obj = Solution()
print(obj.triangleType([1,2,3]))
print(obj.triangleType([3,3,3,]))
print(obj.triangleType([3,4,5]))
print(obj.triangleType([3,3,5]))
