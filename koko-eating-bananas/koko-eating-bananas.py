class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        res = right
        
        while left <= right:
            mid = left + (right - left) // 2

            htaken = 0
            for p in piles:
                htaken += math.ceil(p / mid)

            if htaken > h:
                left = mid + 1
            elif htaken <= h:
                right = mid - 1
                res = mid

        return res
