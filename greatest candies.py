class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        n= len(candies)
        maxi=max(candies)
        result=[]
        for i in range(n):
            if candies[i]+extraCandies>=maxi:
                result.append(True)
            else:
                result.append(False)
        return result