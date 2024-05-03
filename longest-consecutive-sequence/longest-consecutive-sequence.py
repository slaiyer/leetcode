class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        nums2 = set(nums)
        longest = 0

        for n in nums2:
            # check for start of sequence
            if (n - 1) not in nums2:
                length = 1
                while (n + length) in nums2:
                    length += 1

                longest = max(length, longest)

        return longest
