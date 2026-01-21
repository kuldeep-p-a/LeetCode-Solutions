class Solution(object):
    def countKeyChanges(self, s):
        count=0
        s_lower = s.lower()
        for i in range(0, len(s_lower)-1):
            if s_lower[i]!=s_lower[i+1]:
                count+=1
        return count
obj = Solution()
print(obj.countKeyChanges("aAbBcC"))
print(obj.countKeyChanges("AaAaAaaA"))
print(obj.countKeyChanges("AbCdefgh"))