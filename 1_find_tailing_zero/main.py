"""
เขียบนโปรแกรมหาจำนวนเลข 0 ที่ออยู่ติดกันหลังสุดของค่า factorial โดยห้ามใช้ function from math

[Input]
number: as an integer

[Output]
count: count of tailing zero as an integer

[Example 1]
input = 7
output = 1

[Example 2]
input = -10
output = number can not be negative
"""


class Solution:

    def find_tailing_zeroes(self, number: int) -> int | str:
        if '-' not in str(number):
            sum_num = 1
            num_lists = list(int(number) - i for i in range(int(number)) if i < int(number))
            for n in num_lists:
                sum_num *= n
            return "output = %s"%sum_num
        else:
            return "output = number can not be negative"
        
    input_num = input('input = ')
    print(find_tailing_zeroes(1,input_num))