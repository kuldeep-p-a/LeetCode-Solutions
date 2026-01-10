class Solution(object):
    def differenceOfSum(self, nums):
        import numpy as np
        nums_array = np.array(nums)
        el_sum = 0
        for num in nums_array:
            el_sum = el_sum+num
        string_list = [str(num) for num in nums]
        final_str= ""
        for num_str in string_list:
            final_str = final_str+num_str
        digit_sum=0
        for i in range(0, len(final_str)):
            str_i = final_str[i]
            int_i = int(str_i)
            digit_sum = digit_sum+int_i
        return (el_sum-digit_sum)
    

obj = Solution()
print(obj.differenceOfSum([1,15,6,3]))
print(obj.differenceOfSum([1,2,3,4]))