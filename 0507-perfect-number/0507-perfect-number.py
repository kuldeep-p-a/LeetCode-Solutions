class Solution(object):
    def checkPerfectNumber(self, num):
        if num <= 1:
            return False

        total = 1  # 1 is always a divisor

        i = 2
        while i * i <= num:
            if num % i == 0:
                total += i
                if i != num // i:
                    total += num // i
            i += 1

        return total == num   
obj = Solution()
print(obj.checkPerfectNumber(28))
print(obj.checkPerfectNumber(7))
print(obj.checkPerfectNumber(30402457))
