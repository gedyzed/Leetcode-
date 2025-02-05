class Solution:
    def intToRoman(self, num: int) -> str:

        nums = list(map(int, list(str(num))))
        value_symbol = {
            1 : "I",
            4 : 'IV',
            5 : 'V',
            9 : "IX",
            10 : 'X',
            40 : 'XL',
            50 : 'L',
            90 : 'XC',
            100 : 'C',
            400 : 'CD',
            500 : 'D',
            900 : 'CM',
            1000 : 'M'
        }
        result = []
        e = len(nums) - 1 
        for num in nums:
            m = pow(10, e)
            if num * m in value_symbol:
                result.append(value_symbol[num * m])     
            elif num < 5:
                result.append(value_symbol[m] * num ) 
            elif num > 5 :
                result.append(value_symbol[5 * m])
                result.append((num - 5) * value_symbol[m]) 
            e -= 1

        return "".join(result)    


        