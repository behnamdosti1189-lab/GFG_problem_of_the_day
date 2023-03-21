class Solution:
    def minimumTime(self, N : int, cur : int, pos : List[int], time : List[int]) -> int:
        # code here
        mini = 1E9
        for i in range(N):
            mini = min(mini,abs(cur-pos[i])*time[i])
        return mini
