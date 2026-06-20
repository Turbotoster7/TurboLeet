class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        max_sum = sum(nums[:k])
        actual_sum = max_sum
        for right in range(k, len(nums)):
            actual_sum += nums[right] - nums[right - k]
            max_sum = max(actual_sum, max_sum)
        return max_sum / float(k)

nums = [1,12,-5,-6,50,3]
k = 4
s = Solution()
print(s.findMaxAverage(nums, k))