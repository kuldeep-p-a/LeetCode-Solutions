class Solution(object):
    def calPoints(self, operations):
        total = 0
        final_list = []
        for i in range (0, len(operations)):
            if operations[i].lstrip('-+').isdigit():
                final_list.append(int(operations[i]))
                # print(total)
            else:
                if operations[i]=="D":
                    final_list.append(final_list[len(final_list)-1]*2)
                elif operations[i] == "C":
                    final_list.pop(len(final_list)-1)
                    # minus_point = int(final_list[i-1])*-1
                    # final_list.append(minus_point)
                elif operations[i] == "+":
                    p = final_list[len(final_list)-1]
                    q = final_list[len(final_list)-2]
                    r = p+q
                    final_list.append(r)
        print(final_list)
        int_list = [int(a) for a in final_list]
        for num in int_list:
            total = total+num
        return total
        
obj = Solution()
print(obj.calPoints(["5","2","C","D","+"]))
print(obj.calPoints(["5","-2","4","C","D","9","+","+"]))
print(obj.calPoints(["1","C"]))
