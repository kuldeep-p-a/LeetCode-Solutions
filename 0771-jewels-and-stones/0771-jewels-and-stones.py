class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        count = 0
        # if len(stones)>=len(jewels):
        for i in range (0,len(jewels)):
            for j in range (0, len(stones)):
                if jewels[i]==stones[j]:
                    count += 1
        # else:
        #     for i in range (0,len(stones)):
        #         for j in range (0, len(jewels)):
        #             if jewels[i]==stones[j]:
        #                 count += 1
            
        return count
obj = Solution()
print(obj.numJewelsInStones("aA", "aAAbbbb"))
print(obj.numJewelsInStones("z", "ZZ"))