class Solution(object):
    def differenceOfSums(self, n, m):
        num_list = []
        num1 = 0
        num2 = 0
        for i in range (1, n+1):
            num_list.append(i)
#       print (str_list)
        for num in num_list:
            if num%m !=0:
                num1 = num1+num
            else:
                num2 = num2+num
        return (num1-num2)
    
obj = Solution()
print(obj.differenceOfSums(10,3))
print(obj.differenceOfSums(5,6))
print(obj.differenceOfSums(5,1))