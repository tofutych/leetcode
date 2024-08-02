class Solution(object):
    def lengthOfLastWord(self, s):
        return len(s.rsplit(maxsplit=1)[-1])
