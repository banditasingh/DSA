class Solution:
   
    def maxSubArraySum(self,arr,N):
        currSum = 0
        maxSum = -1e8
        for i in range(0,N):
            currSum = currSum + arr[i]
            if currSum > maxSum:
                maxSum = currSum
            if currSum < 0:
                currSum = 0
        return maxSum
                
        