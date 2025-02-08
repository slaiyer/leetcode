class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res: list[list[int]] = []

        for idx, neg in enumerate(nums):
            # skip positive integers
            if neg > 0:
                break

            # skip duplicate negative numbers
            if idx > 0 and neg == nums[idx - 1]:
                continue

            l, r = idx + 1, len(nums) - 1
            while l < r:
                sum3 = neg + nums[l] + nums[r]

                if sum3 > 0:
                    r -= 1
                elif sum3 < 0:
                    l += 1
                else:
                    res.append([neg, nums[l], nums[r]])
                    l += 1
                    r -= 1

                    while nums[l] == nums[l - 1] and l < r:
                        l += 1

                    while nums[r] == nums[r + 1] and l < r:
                        r -= 1

        return res
