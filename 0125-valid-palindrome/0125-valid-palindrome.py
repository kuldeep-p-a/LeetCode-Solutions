class Solution():
    def isPalindrome(self,s):
        import re

        filtered_string_regex = re.sub(r'[^a-zA-Z0-9]', '', s)
        final_string = filtered_string_regex.lower()
        palindrome = ""
        for i in range ((len(final_string)-1), -1, -1):
            palindrome = palindrome + final_string[i]
        # print (palindrome, final_string)
        return palindrome == final_string
    
obj = Solution()
print(obj.isPalindrome ("A man, a plan, a canal: Panama"))
print(obj.isPalindrome ("race a car"))
print(obj.isPalindrome (" ")) 