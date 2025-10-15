class Solution(object):
    def addDigits(self, num):
        total = 0
        new_sum = 0

        while num > 0:
            digit = num % 10
            total = total + digit
            num //= 10

        while total > 9:
            new_sum = 0
            while total > 0:
                new_sum = new_sum + (total % 10)
                total //= 10
            total = new_sum
        return total
        print(total)
      

        