class Solution:
    def findMin(self, nums: list[int]) -> int:
        left, right = 0, len(nums) - 1

        cur_min = 5001
        while left <= right:
            mid = left + (right - left) // 2
            nmid = nums[mid]
            cur_min = min(cur_min, nmid)

            # right side has min
            if nmid > nums[right]:
                left = mid + 1
            # left side has min
            else:
                right = mid - 1

        return cur_min
    