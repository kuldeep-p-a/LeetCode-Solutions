class Solution(object):
    def judgeCircle(self, moves):
        r_count = 0
        l_count = 0
        u_count = 0
        d_count = 0
        for i in range (0, len(moves)):
            if moves[i] == "R":
                r_count +=1
            elif moves[i] == "L":
                l_count +=1
            elif moves[i] == "D":
                d_count +=1
            elif moves[i] == "U":
                u_count +=1
        if r_count==l_count and d_count==u_count:
            return True
        else:
            return False
obj = Solution()
print(obj.judgeCircle("DU"))
print(obj.judgeCircle("LL"))
print(obj.judgeCircle("RLRLUDUD"))
print(obj.judgeCircle("RLRLUDUDR"))