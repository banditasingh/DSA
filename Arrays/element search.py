class Solution:
    def search(self,arr, N, X):
        if X in arr:
            return arr.index(X)
        else:
            return -1
        