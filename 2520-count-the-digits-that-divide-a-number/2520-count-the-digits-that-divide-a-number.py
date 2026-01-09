class Solution():
    def countDigits(self, num):
        num_str = str(num)
        num_len = len(num_str)
        count  = 0
        if num_len==0:
            return count
        else:
            for i in range (0,num_len):
                digit_str = num_str[i]
                digit_int = int(digit_str)
                if num%digit_int==0:
                    count+=1
                else:
                    count=count
        return count
               
       
obj = Solution()
print(obj.countDigits(121))
print(obj.countDigits(1248))
print(obj.countDigits(7))
