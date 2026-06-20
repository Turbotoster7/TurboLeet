class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums = sorted(nums)
        solutions = []
        for n in range(len(nums) - 2):

            if nums[n] > 0:
                break

            if nums[n] == nums[n - 1] and n > 0:
                continue

            left = n + 1
            right = len(nums) - 1
            while left < right:
                sum = nums[left] + nums[right] + nums[n]
                if sum == 0:
                    solutions.append([nums[n], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                elif sum > 0:
                    right -= 1
                else:
                    left += 1
        return solutions


nums = [-1,0,1,2,-1,-4]
s = Solution()
print(s.threeSum(nums))