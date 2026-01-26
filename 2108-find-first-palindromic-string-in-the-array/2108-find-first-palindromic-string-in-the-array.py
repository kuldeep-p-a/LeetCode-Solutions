class Solution(object):
    def firstPalindrome(self, words):
        re_word = ""
        for item in words:
            for i in range (len(item)-1, -1, -1):
                re_word = re_word+item[i]
            if item == re_word:
                return item
            else:
                re_word=""
                continue
        return ""
obj = Solution()
print(obj.firstPalindrome(["abc","car","ada","racecar","cool"]))
print(obj.firstPalindrome(["notapalindrome","racecar"]))
