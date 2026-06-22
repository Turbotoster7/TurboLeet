class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        detecs baloons word
        """
        word = {'b': 0, 'a': 0, 'l': 0, 'o': 0, 'n': 0}
        for char in text:
            if char in word:
                word[char] += 1

        word['o'] //= 2
        word['l'] //= 2
        return min(word.values())


s = Solution()
text = "nlaebolko"
print(s.maxNumberOfBalloons(text))