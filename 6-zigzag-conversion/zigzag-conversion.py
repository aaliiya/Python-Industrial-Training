class Solution:
    def convert(self, s, numRows):
        if numRows == 1 or numRows >= len(s):
            return s

        rows = [""] * numRows
        curRow = 0
        direction = -1

        for c in s:
            rows[curRow] += c

            if curRow == 0 or curRow == numRows - 1:
                direction *= -1

            curRow += direction

        return "".join(rows)