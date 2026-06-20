class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        rows = [[] for _ in range(numRows)]
        row, step = 0, 1
        for ch in s:
            rows[row].append(ch)
            if row == 0:
                step = 1
            elif row == numRows - 1:
                step = -1
            row += step
        return "".join("".join(r) for r in rows)

sol = Solution()
s = "PAYPALISHIRING"
numRows = 3
print(sol.convert(s, numRows))

# class Solution:
#     def convert(self, s: str, numRows: int) -> str:
#         output = ""
#         if numRows == 1:
#             return s
#         for row in range(numRows):
#             index = row
#             while index < len(s):
#                 output += s[index]
#                 if row == 0 or row == numRows - 1:
#                     index += 2 * (numRows - 1)
#                 else:
#                     index += 2 * (numRows - 1 - row)
#                 if row != 0 and row != numRows - 1:
#                     if index >= len(s):
#                         break
#                     output += s[index]
#                     index += 2*(row)
#         return output

