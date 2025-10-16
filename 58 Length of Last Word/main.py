class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.strip(" ").split(" ")[-1])

s = Solution()
# s = "Hello World"
string = "   fly me   to   the moon  "
print(s.lengthOfLastWord(string))

# class Solution:
#     def plusOne(self, digits: list[int]) -> list[int]:
#         for i in range(len(digits) - 1, -1, -1):
#             if digits[i] < 9:
#                 digits[i] += 1
#                 return digits
#             digits[i] = 0

        # return [int(digit) for digit in str(int("".join(digits)) + 1)]

# s = Solution()
# digits = [1,2,3]
# print(s.plusOne(digits))