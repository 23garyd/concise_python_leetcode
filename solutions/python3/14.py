class Solution:

    """
    def longestCommonPrefix(self, strs):
        r = [len(set(c)) == 1 for c in zip(*strs)] + [0]
        return strs[0][:r.index(0)] if strs else ''
    """


    def longestCommonPrefix(self, s) -> str:
        j = 0
        while s and all(j < len(s[i]) and j < len(s[i - 1]) and s[i][j] == s[i - 1][j] for i in range(len(s))):
            j += 1
        return s[0][:j] if j else ''

a = Solution()
strs = ['Happy', 'Happen']
res = a.longestCommonPrefix(strs)
print(res)