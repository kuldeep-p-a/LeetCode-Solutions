class Solution(object):
    def subtractProductAndSum(self, n):
        str_n = str(n)
        sum = 0
        product = 1
        for i in range (0, len(str_n)):
            p = int(str_n[i])
            sum = sum+p
            product = product*p
        return product-sum
obj = Solution()
print(obj.subtractProductAndSum(234))
print(obj.subtractProductAndSum(4421))