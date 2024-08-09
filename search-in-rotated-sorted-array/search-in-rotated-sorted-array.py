class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2
            nmid = nums[mid]
            nleft = nums[left]
            nright = nums[right]

            if nmid == target:
                return mid

            if nleft <= nmid:
                if target > nmid or target < nleft:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                if target < nmid or target > nright:
                    right = mid - 1
                else:
                    left = mid + 1

        return -1

        return -1
