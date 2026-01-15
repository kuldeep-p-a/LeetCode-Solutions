class Solution(object):
    def checkIfPangram(self, sentence):
        alphabets = "abcdefghijklmnopqrstuvwxyz"
        for i in range (0, len(alphabets)):
            if alphabets[i] in sentence:
                continue
            else:
                return False
        return True
obj = Solution()
print(obj.checkIfPangram("thequickbrownfoxjumpsoverthelazydog"))
print(obj.checkIfPangram("leetcode"))
print(obj.checkIfPangram("qwertyuioplkjhgfdsazxcvbnm"))