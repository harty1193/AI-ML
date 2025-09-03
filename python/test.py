class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        for i in range(len(nums)):
            if nums[i] == 0:
                nums.pop(i)
                nums.append(0)
        return nums


nums = [0,1,0]

sol = Solution()

print(sol.moveZeroes(nums))