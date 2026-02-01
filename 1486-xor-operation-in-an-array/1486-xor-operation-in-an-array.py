class Solution(object):
    def xorOperation(self, n, start):
        nums = []
        for i in range (0, n):
            x = start+2*i
            nums.append(x)
        # print(nums)
        if len(nums)<2:
            return nums[0]
        p = nums[0]^nums[1]
        if len(nums) == 2:
            return p
        else:
            for i in range (2, len(nums)):
                p=p^nums[i]
        return (p)
obj = Solution()
print(obj.xorOperation(5,0))
print(obj.xorOperation(4,3))
print(obj.xorOperation(1,0)) 

        