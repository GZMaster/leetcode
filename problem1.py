class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        for i, num in enumerate(nums):
            if target - num in nums[i + 1 :]:
                return [i, nums[i + 1 :].index(target - num) + i + 1]

        print("No two sum solution")
        return None


__main__ = Solution()
nums = [2, 7, 11, 15]
target = 9
print(__main__.twoSum(nums, target))
