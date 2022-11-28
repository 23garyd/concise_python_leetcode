import re


class Solution:
    def myAtoi(self, s):
        arr = re.findall('[\+\-]?\d+', s.lstrip())[0]
        return max(min(int(arr, s.lstrip()), 2 ** 31 - 1), -2 ** 31)

a = Solution()
r = a.myAtoi("$$$$&+1323")
print(r)