class Solution:
    def myAtoi(self, s: str) -> int:
        oper = {'-', '+'}  
        lower_limit = -2 ** 31
        upper_limit = 2 ** 31 - 1

        result, s = [], s.strip()  

        for char in s:
            if char in oper and not result:  
                result.append(char)
            elif char.isdigit():
                result.append(char)
            else:
                break 

        if len(result) == 1 and result[0] in oper:
            return 0  

        num = int("".join(result)) if result else 0
        if num < lower_limit:
            return lower_limit
        if num > upper_limit:
            return upper_limit

        return num
