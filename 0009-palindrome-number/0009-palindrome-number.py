class Solution():
    def isPalindrome(self, x):
        string_integer = str(x)
        new_integer = ""
        for i in range ((len(string_integer)-1), -1, -1):
            new_integer = new_integer + string_integer[i]
        return string_integer == new_integer
obj = Solution()
print(obj.isPalindrome(121))
print(obj.isPalindrome(-121))
print(obj.isPalindrome(10))     