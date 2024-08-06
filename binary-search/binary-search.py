class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + ((right - left) // 2)  # (l + r) // 2 can lead to overflow

            if (check := nums[mid]) < target:
                left = mid + 1
            elif check > target:
                right = mid - 1
            else:
                return mid

        return -1
