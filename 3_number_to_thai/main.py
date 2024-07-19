"""
เขียบนโปรแกรมแปลงตัวเลยเป็นคำอ่านภาษาไทย

[Input]
number: positive number rang from 0 to 10_000_000

[Output]
num_text: string of thai number call

[Example 1]
input = 101
output = หนึ่งร้อยเอ็ด

[Example 2]
input = -1
output = number can not less than 0
"""


class Solution:

    def number_to_thai(self, number: int) -> str:
        num_thai = ""
        thai_unit1 = ["ศูนย์", "หนึ่ง", "สอง", "สาม", "สี่", "ห้า", "หก", "เจ็ด", "แปด", "เก้า"]
        thai_unit2 =["", "สิบ", "ร้อย", "พัน", "หมื่น", "แสน", "ล้าน"]
        if '-' not in str(number):
            if len(str(number)) == 1:
                num_thai = thai_unit1[int(number)]
            elif len(str(number)) == 2:
                if int(str(number)[0]) >= 2:
                    if int(str(number)[0]) == 2:
                        n = "ยี่"
                        num_thai += n + thai_unit2[1]
                    else:
                        num_thai += thai_unit1[int(str(number)[0])] + thai_unit2[1]
                    if int(str(number)[1]) == 1:
                        num_thai += "เอ็ด"
                    else:
                        if int(str(number)[1]) != 0:
                            num_thai += thai_unit1[int(str(number)[1])]
                else:
                    num_thai += thai_unit2[int(str(number)[0])]
                    if int(str(number)[1]) == 1:
                        n = "เอ็ด" 
                        num_thai += n
            elif len(str(number)) == 3:
                num_thai += thai_unit1[int(str(number)[0])]
                num_thai += thai_unit2[2]
                if int(str(number)[1]) > 0:
                    if int(str(number)[1]) == 2:
                        n = "ยี่"
                        num_thai += n + thai_unit2[1]
                    else:
                        num_thai += thai_unit1[int(str(number)[1])] + thai_unit2[1]
                    if int(str(number)[2]) != 0:
                        num_thai += thai_unit1[int(str(number)[2])]
                else:
                    if int(str(number)[2]) != 0:
                        num_thai += thai_unit1[int(str(number)[2])]
            else:
                num_thai = "No information found."
        else:
            num_thai = "number can not less than 0"
        return "output = %s"%num_thai
    
    numbers = input('input = ')
    print(number_to_thai(1,numbers))
