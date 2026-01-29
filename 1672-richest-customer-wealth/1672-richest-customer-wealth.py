class Solution(object):
    def maximumWealth(self, accounts):
        money_list = []
        wealth = 0
        for person in accounts:
            for money in person:
                wealth = wealth + money
            money_list.append(wealth)
            wealth = 0
        money_list.sort()
        return (money_list[-1])
obj = Solution()
print(obj.maximumWealth([[1,2,3],[3,2,1]]))
print(obj.maximumWealth([[1,5],[7,3],[3,5]]))
print(obj.maximumWealth([[2,8,7],[7,1,3],[1,9,5]]))