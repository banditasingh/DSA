
class Solution:
    def zigZag(self, arr, n):
        for i in range(n-1):
            j = i + 1
            if i% 2== 0:
                if arr[i] > arr[j]:
                    t = arr[i] 
                    arr[i] = arr[j]
                    arr[j] = t
            else:
                if arr[i] < arr[j]:
                    t = arr[i] 
                    arr[i] = arr[j]
                    arr[j] = t
                    