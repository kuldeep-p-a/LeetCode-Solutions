class Solution(object):
    def threeConsecutiveOdds(self, arr):
        count = 0
        for i in range (0, len(arr)-2):
            if arr[i]%2 != 0:
                if arr[i+1]%2 != 0:
                    if arr[i+2]%2 !=0:
                        count=count+1
            else:
                continue
        if count>0:
            return True
        else:
            return False
obj = Solution()
print(obj.threeConsecutiveOdds([2,6,4,1]))
print(obj.threeConsecutiveOdds([1,2,34,3,4,5,7,23,12]))