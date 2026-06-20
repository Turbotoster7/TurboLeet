# 3614. Process String with Special Operations II
class Solution:
    def processStr(self, s: str, k: int) -> str:
        length = 0
        for instruction in s:
            if instruction == "#":
                length *= 2
            elif instruction == "%":
                pass
            elif instruction == "*":
                length = max(0, length - 1)
            else:
                length += 1
        if k >= length:
            return "."
        for instruction in reversed(s):
            if instruction.islower():
                if k == length - 1:
                    return instruction
                length -= 1
            elif instruction == "#":
                length //= 2
                if k >= length:
                    k -= length
            elif instruction == "%":
                k = length - 1 - k
            elif instruction == "*":
                length += 1
        return "."





# aaaaaaabbbbbbbbddeeeeee
#



sol = Solution()
s = "z*#"
k = 0
print(sol.processStr(s, k))