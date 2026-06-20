#include <algorithm>
#include <vector>

class Solution {
    public:
        std::vector<int> twoSum(std::vector<int>& nums, int target) {
            std::sort(nums.begin(), nums.end());
            for (auto i = 0;  nums.size(); i++)
            {
                if (nums[i] >= target)
                {
                    return std::vector<int> {};
                }
                for (auto a = i; a <= nums.size(); a++)
                {
                    if (nums[a] + nums[i] == target)
                    {
                        return std::vector<int> {nums[a], nums[i]};
                    }
                }
            }
        }
    };

int main() {
    Solution s;
    std::vector<int> nums = {2, 7, 11, 15};
    auto result = s.twoSum(nums, 9);
    return 0;
}