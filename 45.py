from collections import deque



class Solution:
    def jump(self, nums) -> int:
        # if len(nums) == 1:
        #     return 0
        # q = deque()
        # q.append(0)
        # visited = {}
        # visited[0] = 0
        # while q:
        #     number = q.popleft()
        #     for n in range(1, nums[number] + 1):
        #         next_idx = number + n
        #         if next_idx >= len(nums):
        #             break
        #         if next_idx == len(nums) - 1:
        #             return visited[number] + 1
        #         if next_idx not in visited:
        #             visited[next_idx] = visited[number] + 1
        #             q.append(next_idx)

        # return visited[len(nums) - 1]
        
        if len(nums) == 1:
            return 0
        jumps = 0
        current_end = 0
        farthest = 0
        for n in range(len(nums) - 1):
            farthest = max(farthest, n + nums[n])
            if n == current_end:
                current_end = farthest
                jumps += 1
        return jumps

s = Solution()
nums = [2,3,1,1,4]
print(s.jump(nums))