class Solution:
    def reverse(self, x):
        y = int(str(x)[::-1]) if x >= 0 else int("-" + str(x)[::-1][:-1])
        return -2 ** 31 <= y <= 2 ** 31 - 1 and y or 0


a = Solution()
tt = a.reverse(-123)
print(tt)