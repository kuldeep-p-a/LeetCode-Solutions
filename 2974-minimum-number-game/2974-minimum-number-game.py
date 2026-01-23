class Solution(object):
    def numberGame(self, nums):
        arr=[]
        nums.sort()
        while len(nums)>0:
            
            
            al = nums.pop(0)
            # nums.remove(al)
            bob = nums.pop(0)
            # nums.remove(bob)
            arr.append(bob)
            arr.append(al)
            print(arr)

            
            
        return arr
obj = Solution()
print(obj.numberGame([5,4,2,3]))
