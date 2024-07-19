"""
เขียบนโปรแกรมแปลงตัวเลยเป็นตัวเลข roman

[Input]
number: list of numbers

[Output]
roman_text: roman number

[Example 1]
input = 101
output = CI

[Example 2]
input = -1
output = number can not less than 0
"""


class Solution:

    def number_to_roman(self, number: int) -> str:
        roman_dict = {1: 'I', 5: 'V', 10: 'X', 50: 'L'}
        num = [1000, 900, 500, 400,100, 90, 50, 40,10, 9, 5, 4,1]
        roman = ["M", "CM", "D", "CD","C", "XC", "L", "XL","X", "IX", "V", "IV","I"]
        result = ""
        for i in range(len(num)):
            while number >= num[i]:
                result += roman[i]
                number -= num[i]
        return "output = %s"%result

    input_num = int(input('input = '))
    print(number_to_roman(1,input_num))