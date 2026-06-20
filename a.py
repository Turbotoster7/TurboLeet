class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # for n in range(len(nums) - 1):
        #     if nums[n] >= target:
        #         continue
        #     for i in range(n+1, len(nums)):
        #         if nums[n] + nums[i] == target:
        #             return [n, i]
        visited = {}
        for pos, num in enumerate(nums):
                needed = target - num
                if needed in visited:
                    return [visited[needed], pos]
                visited[num] = pos



nums = [3, 3]
target = 6
s = Solution()
print(s.twoSum(nums, target))