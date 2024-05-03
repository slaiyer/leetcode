class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        rev_map: dict[int, int] = {}  # val -> idx

        for idx, n in enumerate(nums):
            diff = target - n

            if diff in rev_map:
                return [rev_map[diff], idx]

            rev_map[n] = idx

        return [-1, -1]
