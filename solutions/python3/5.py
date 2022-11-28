class Solution:
    def longestPalindrome(self, s: str) -> str:
        def check(l, r):
            while 0 <= l <= r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            print(s[l + 1:r])
            return s[l + 1:r]
        pals = [check(i, i) for i in range(len(s))]
        second = [check(i, i + 1) for i in range(len(s) - 1) if s[i] == s[i + 1]]
        return sorted(pals + second, key = len)[-1] if pals else ''

a = Solution()
res = a.longestPalindrome("baaaaaaabad")
print(res)