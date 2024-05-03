class Solution:
    def trap(self, height: list[int]) -> int:
        water = 0

        l, r = 0, len(height) - 1
        l_wall, r_wall = height[l], height[r]

        while l < r:
            if l_wall < r_wall:
                l += 1
                l_wall = max(l_wall, height[l])
                water += l_wall - height[l]
            else:
                r -= 1
                r_wall = max(r_wall, height[r])
                water += r_wall - height[r]

        return water
