class Solution:

    def letterCombinations(self, digits):
        dic, res = { '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}, [""]
        for dig in digits:
            tmp = []
            for y in res: 
                for x in dic[dig]:
                    tmp.append(y + x)
            res = tmp 
        return res if any(res) else []

    '''

    def letterCombinations(self, digits):
        if not digits:
            return []
        phone_dict = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        def backtrack(combination, index):
            if index == len(digits):
                combinations.append(combination)
            else:
                digit = digits[index]
                for letter in phone_dict[digit]:
                    backtrack(combination + letter, index + 1)

        combinations = list()
        backtrack('', 0)
        return combinations
    '''

a = Solution()
res = a.letterCombinations("23")
print(res)
