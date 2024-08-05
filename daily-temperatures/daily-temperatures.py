class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        st = []

        for ti, t in enumerate(temperatures):
            while len(st) > 0:
                topi = st[-1]

                if temperatures[topi] >= t:
                    break
                
                ans[topi] = ti - topi
                st.pop()
            
            st.append(ti)

        return ans
