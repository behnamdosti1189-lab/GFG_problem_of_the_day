class Solution():
    def maxWeightCell(self, N, Edge):
        #your code goes here
        weight = [0] * N
        for i in range(N):
            if Edge[i] != -1:
                weight[Edge[i]] += i
        max_weight = max(weight)
        max_index = N - 1
        for i in range(N - 1, -1, -1):
            if weight[i] == max_weight:
                max_index = i
                break
        return max_index
