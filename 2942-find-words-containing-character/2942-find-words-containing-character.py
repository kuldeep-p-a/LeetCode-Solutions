class Solution(object):
    def findWordsContaining(self, words, x):
        new_list = []
        for i in range (0, len(words)):
            for j in range (0, len(words[i])):
                if words[i][j] == x:
                    new_list.append(i)
                    break
        return new_list
obj = Solution()
print(obj.findWordsContaining(["leet","code"], "e"))
print(obj.findWordsContaining(["abc","bcd","aaaa","cbc"], "a"))
print(obj.findWordsContaining(["abc","bcd","aaaa","cbc"], "z"))
        