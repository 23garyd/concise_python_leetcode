class Solution:
    '''
    def intToRoman(self, num):
        s = "M" * (num // 1000)
        s += "CM" if num % 1000 >= 900 else "D" *((num % 1000) // 500)
        s += "CD" if num % 500 >= 400 and s[-2:] != "CM" else "C" * ((num % 500) // 100)  if num % 500 < 400 else ""
        s += "XC" if num % 100 >= 90 else "L" * ((num % 100) // 50)
        s += "XL" if num % 50 >= 40 and s[-2:] != "XC" else "X" * ((num % 50) // 10)  if num % 50 < 40 else ""
        s += "IX" if num % 10 >= 9 else "V" * ((num % 10) // 5)
        s += "IV" if num % 5 >= 4 and s[-2:] != "IX" else "I" * ((num % 5) // 1) if num % 5 < 4 else ""
        return s
    '''


    def intToRoman(self, num: int) -> str:
        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        romans = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        res, i = '', 0
        while num:
            res += num // values[i] * romans[i]
            num = num % values[i]
            i += 1
        return res



a = Solution()
res = a.intToRoman(3444)
print(res)

