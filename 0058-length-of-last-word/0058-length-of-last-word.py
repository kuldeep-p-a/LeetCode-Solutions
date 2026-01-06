class Solution():
    def lengthOfLastWord(self, s):
        new_s = s.rstrip()
        added_s = " "+new_s
        final_s = added_s.rstrip("!@#$%^&*?.,")
        for i in range (len(final_s)-1, -1, -1):
            if final_s[i] == " ":
                last_word = final_s [i+1:len(final_s)]
                break
        print(last_word)
        return (len(last_word))

obj = Solution()
print(obj.lengthOfLastWord("Hello World"))
print(obj.lengthOfLastWord("   fly me   to   the moon  "))
print(obj.lengthOfLastWord("luffy is still joyboy"))