class Solution(object):
    def firstUniqChar(self, s):
        freq = {}

        # Step 1: Count frequency of each character
        for ch in s:
            if ch in freq:
                freq[ch] += 1
            else:
                freq[ch] = 1

        # Step 2: Find first character with count 1
        for i in range(len(s)):
            if freq[s[i]] == 1:
                return i

        return -1

obj = Solution()
print(obj.firstUniqChar("leetcode"))
print(obj.firstUniqChar("loveleetcode"))
print(obj.firstUniqChar("aab"))