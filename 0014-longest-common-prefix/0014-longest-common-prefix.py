class Solution():
    def longestCommonPrefix(self, strs):
        common_str = ""
        
        if len(strs) == 0:
            return ""
        elif len(strs) == 1:
            return strs[0]
        elif len(strs) == 2:
            str1 = strs[0]
            str2 = strs[1]
            for char in range (0, min(len(str1), len(str2))):
                if str1[char]==str2[char]:
                    common_str = common_str+str1[char]
                else:
                    break
            return common_str
        else:
            str1 = strs[0]
            str2 = strs[1]
            for char in range (0, min(len(str1), len(str2))):
                if str1[char]==str2[char]:
                    common_str = common_str+str1[char]
                else:
                    break
            if len(common_str) == 0:
                return ""
            elif len(common_str) != 0:
            
                for i in range (2, len(strs)):
                    common_str2 = ""
                    for j in range (0, min(len(strs[i]), len(common_str))):
                        if strs[i][j]==common_str[j]:
                                common_str2 = common_str2+common_str[j]
                        else:
                            break
                    common_str = common_str2
                return common_str
obj = Solution()
print(obj.longestCommonPrefix(["flower","flow","flight"]))
print(obj.longestCommonPrefix(["dog","racecar","car"]))
print(obj.longestCommonPrefix(["a", "ab"]))
print(obj.longestCommonPrefix(["test","test","test","test","test"]))
print(obj.longestCommonPrefix(["baab","bacb","b","cbc"]))
print(obj.longestCommonPrefix([""]))
print(obj.longestCommonPrefix(["test","tester","testing","tested","testis"]))
print(obj.longestCommonPrefix(["abca", "abc", "abx", "ab"]))
print(obj.longestCommonPrefix(["", "abc"]))
print(obj.longestCommonPrefix(["interview", "internet", "internal", "cat"]))