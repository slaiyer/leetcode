class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        res = [1] * (len(nums))

        # forward accumulative product through index i - 1
        for i in range(1, len(nums)):
            res[i] = res[i - 1] * nums[i - 1]

        # reverse accumulative product
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]

        return res
