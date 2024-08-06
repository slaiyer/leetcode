class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        st: list[tuple[int, int]] = []  # (index, height)

        for i, h in enumerate(heights):
            start = i
            while st and st[-1][1] >= h:
                ti, th = st.pop()
                max_area = max(max_area, th * (i - ti))
                start = ti
            st.append((start, h))

        for i, h in st:
            max_area = max(max_area, h * (len(heights) - i))

        return max_area
