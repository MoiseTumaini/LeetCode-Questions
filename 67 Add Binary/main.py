class Solution:
    def addBinary(self, a:str, b:str) -> str:
        carry = 0

        result = []

        if len(a) > len(b):
            b = (len(a) - len(b))*"0" + b
        else:
            a = (len(b) - len(a))*"0" + a
        

        for i in range(len(a) - 1, -1 , -1):
            total = int(a[i]) + int(b[i]) + carry

            sum_bit = total%2
            carry = total//2

            result.append(str(sum_bit))


        if carry > 0:
            result.append(str(carry))


        return "".join(result)[::-1]
    
    
s = Solution()

print(s.addBinary("11" ,"1"))



        



