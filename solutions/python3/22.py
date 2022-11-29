class Solution:
    # def generateParenthesis(self, n: int) -> List[str]:
    #     bfs = [(0, 0, '')]
    #     for c in range(n * 2):
    #         bfs = [(l + 1, r, s + '(') for l, r, s in bfs if l + 1 <= n] + [(l, r + 1, s + ')') for l, r, s in bfs if l - r]
    #     return [s for l, r, s in bfs]

    def helpler(self, l, r, item, res):
        if r < l:
            # print item
            return
        if l == 0 and r == 0:
            res.append(item)
        if l > 0:
            self.helpler(l - 1, r, item + '(', res)
        if r > 0:
            self.helpler(l, r - 1, item + ')', res)


    def generateParenthesis(self, n):
        """ :type n: int :rtype: List[str] """
        if n == 0:
            return []
        res = []
        self.helpler(n, n, '', res)
        return res

a = Solution()
res = a.generateParenthesis(3)
print(res)