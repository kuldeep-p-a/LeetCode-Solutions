class Solution(object):
    def mostWordsFound(self, sentences):
        word_list = []
        count = 0
        for sentence in sentences:
            for char in sentence:
                if char == " ":
                    count+=1
            word_list.append(count)
            count=0
        word_list.sort()
        return (word_list[-1]+1)
obj = Solution()
print(obj.mostWordsFound(["alice and bob love leetcode", "i think so too", "this is great thanks very much"]))
print(obj.mostWordsFound(["please wait", "continue to fight", "continue to win"]))