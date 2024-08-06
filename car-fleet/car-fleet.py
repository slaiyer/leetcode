class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        h = sorted(list(zip(position, speed)), reverse=True)
        st: list[float] = []  # times to reach target

        for p, s in h:
            st.append((target - p) / s)
            if len(st) > 1 and st[-1] <= st[-2]:
                st.pop()

        return len(st)
