class Solution:
    def equilibriumPoint(self,A, N):
        if N == 1:
            return 1
        left_sum = 0
        total_sum = sum(A)
      
        for j in range(N):
            if left_sum == total_sum-A[j]:
                return j+1
            left_sum += A[j]
            total_sum -= A[j]
        return -1