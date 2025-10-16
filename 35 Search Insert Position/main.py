class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        
        # if target in nums:

        # for i in range(len(nums)):
        #     if nums[i] >= target:
        #         return i

        i = 0

        while True:
            if nums[i] >= target:
                return i
            elif i == len(nums) - 1:
                return i + 1
            else:
                i += 1
s = Solution()

# nums = [1,3,5,6]
# target = 5
# print(s.searchInsert(nums, target))

# nums = [1,3,5,6]
# target = 2
# print(s.searchInsert(nums, target))

nums = [1,3,5,6]
target = 7
print(s.searchInsert(nums, target))




