class Solution:
    def moveZeroes(self, nums):
        pos = 0  # position for next non-zero

        # Move non-zero elements forward
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[pos] = nums[i]
                pos += 1

        # Fill the rest with zeros
        for i in range(pos, len(nums)):
            nums[i] = 0
