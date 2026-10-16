class Solution(object):
    def reverse(self, x):
        new_str = ""
        if x > 0:
            x_str = str(x)
            for i in range (len(x_str)-1, -1, -1):
                new_str = new_str + x_str[i]
            new_int = int(new_str)
        if x < 0:
            x = x*(-1)
            x_str = str(x)
            for i in range (len(x_str)-1, -1, -1):
                new_str = new_str + x_str[i]
            
            new_int = int(new_str)*-1
        if x == 0 or new_int < -2**31 or new_int > 2**31:
            new_int = 0
        return new_int

            

