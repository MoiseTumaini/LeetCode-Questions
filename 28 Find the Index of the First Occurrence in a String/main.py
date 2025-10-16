class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(haystack) < 1 or len(needle) > 104 or needle not in haystack:
            return -1
        
        start = 0
        ii = 0
        
        cond = False

        while not cond:
            count = 0
            ii = start
            for i in range(len(needle)):
                if haystack[ii] == needle[i]:
                    ii += 1
                    count += 1
                    continue

            if count == len(needle):
                cond = True
            else:
                start += 1

        return start 
        
        
s = Solution()

print(s.strStr("mississippi", "issip"))  # Output: 4
print(s.strStr("aaaaa", "bba")) # Output: -1