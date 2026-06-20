class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        # left = 0
        # current_sum = 0
        # min_len = len(nums) + 1

        # for right in range(len(nums)):
        #     current_sum += nums[right]

        #     while current_sum >= target:
        #         min_len = min(right - left + 1, min_len)
        #         current_sum -= nums[left]
        #         left += 1

        # if min_len == len(nums) + 1:
        #     return 0

        # return min_len
        n = len(nums)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[n+1] = prefix[n] + nums[n]

        min_len = len(nums) + 1
        for i in range(n):
            needed = prefix[i] + target
            j = bisect.bisect_left(prefix, needed)
            if j <= n:
                min_len = min(min_len, j - i)

        return min_len if min_len <= n else 0

target = 11
nums = [1, 2, 3, 4, 5]
s = Solution()
print(s.minSubArrayLen(target, nums))
