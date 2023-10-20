#divisble by 3 using array digits

class Solution:
    def isPossible(self, N, arr):
        if sum(arr)%3 == 0:
            return 1 
        else: 
            return 0