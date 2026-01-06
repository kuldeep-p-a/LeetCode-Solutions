class Solution():
    def plusOne(self, digits):
        import array as arr
        import numpy as np
        list_one = list(digits)
        string_integer = ""
        for i in list_one:
           string_integer = string_integer+str(i)
        the_integer = int(string_integer)
        new_interger = the_integer + 1
        new_sting_integer = str(new_interger)
        new_list = []
        for i in new_sting_integer:
            new_list.append(int(i))
        final_array = np.array(new_list)
        return new_list

obj = Solution()
print(obj.plusOne([1,2,3]))
print(obj.plusOne([4,3,2,1]))
print(obj.plusOne([9]))