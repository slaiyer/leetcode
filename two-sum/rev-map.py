class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        rev_map: dict[int, int] = {}  # val -> idx

        for idx, n in enumerate(nums):
            diff = target - n

            if diff in rev_map:
                return [rev_map[diff], idx]

            rev_map[n] = idx
