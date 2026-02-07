class Solution(object):
    def isPowerOfFour(self, n):
        
        if n <=4:
            if n == 4 or n ==1:
                return True
            else:
                return False
        elif n>4:
            if n%4!=0:
                return False
            else:
                while (n%4)==0:
                    # if n%4 == 0:
                        n=n//4
                        if n == 1:
                            return True
                        else:
                            continue
                return False
obj = Solution()
print(obj.isPowerOfFour(5))
print(obj.isPowerOfFour(16))
print(obj.isPowerOfFour(0))
print(obj.isPowerOfFour(1))
print(obj.isPowerOfFour(4))
        