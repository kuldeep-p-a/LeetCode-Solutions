class Solution(object):
    def numberOfEmployeesWhoMetTarget(self, hours, target):
        count = 0
        for time in hours:
            if time>=target:
                count+=1
        return count
obj = Solution()
print(obj.numberOfEmployeesWhoMetTarget([0,1,2,3,4], 2))
print(obj.numberOfEmployeesWhoMetTarget([5,1,4,2,2], 6))