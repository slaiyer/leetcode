class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        checkboxes: set[int] = set()
        for num in nums:
            if num in checkboxes:
                return True
            else:
                checkboxes.add(num)

        return False
