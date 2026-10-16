class Solution(object):
    def rotate(self, matrix):
        list1 = []
        
        for i in range (0, len(matrix[0])):
            list2 = []
            for j in range (-1, (len(matrix)+1)*-1, -1):
                list2.append(matrix[j][i])
            list1.append(list2)
        matrix[:] = list1 
        