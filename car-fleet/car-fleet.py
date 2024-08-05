class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        h = sorted(list(zip(position, speed)), reverse=True)
        st = []  # times to reach target
        
        for p, s in h:
            st.append((target - p) / s)
            if len(st) > 1 and st[-1] <= st[-2]:
                st.pop()
        
        return len(st)
