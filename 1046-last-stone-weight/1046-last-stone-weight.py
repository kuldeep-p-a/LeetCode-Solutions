class Solution(object):
    def lastStoneWeight(self, stones):
        # import copy
        if len(stones)==1:
            return stones[0]
        else:
            copy_s = stones[:]
            while len(stones)>1:
                copy_s.sort()
                y = copy_s[-1]
                x = copy_s[-2]
                stones.remove(x)
                stones.remove(y)
                copy_s.remove(x)
                copy_s.remove(y)
                if x == y:
                    continue
                elif x!=y:
                    stones.append(y-x)
                copy_s = stones[:]
            return stones[0] if stones else 0
obj = Solution()
print(obj.lastStoneWeight([2,7,4,1,8,1]))
    
       