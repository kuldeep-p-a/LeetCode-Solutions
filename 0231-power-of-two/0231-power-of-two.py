class Solution(object):
    def isPowerOfTwo(self, n):
        if n > 1 and n % 2 != 0:
            return False
        if n <= 0:
            return False
        if n == 2 or n == 1:
            return True
        while n >= 2:  
            if n%2==0:
                n = n//2
                # print (n)
                continue
            elif n %2 !=0:
                # print(n)
                return False
        return True
       
obj = Solution()
print(obj.isPowerOfTwo(1))
print(obj.isPowerOfTwo(16)) 
print(obj.isPowerOfTwo(3))  
