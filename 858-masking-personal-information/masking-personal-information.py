class Solution:
    def maskPII(self, s: str) -> str:

        def mask_email(s):
            name, domain = s.split('@')
            first, last = name[0].lower(), name[-1].lower()
            return f"{first}*****{last}@{domain.lower()}"

        def mask_phone_number(s):
            nums = "".join([char for char in s if char.isdigit()])  
            front = ""
            if len(nums) > 10:
                front = f"+{'*' * (len(nums) - 10)}-"

            return f"{front}***-***-{nums[-4:]}"

        if s[0].isalpha():
            return mask_email(s)                  
        return mask_phone_number(s)     

        