class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        total = 0
        for number in range(len(s)):
            if number + 1 < len(s) and roman[s[number]] < roman[s[number + 1]]:
                total -= roman[s[number]]
            else:
                total += roman[s[number]]

        return total