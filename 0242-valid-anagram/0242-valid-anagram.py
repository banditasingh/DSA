class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sss = sorted(s)
        ttt = sorted(t)
        return sss == ttt
    