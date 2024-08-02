class Solution(object):
    def reverse(self, x):
        reversed_x = int(str(abs(x))[::-1])
        return (
            (reversed_x if x > 0 else -reversed_x)
            if reversed_x.bit_length() < 32
            else 0
        )
