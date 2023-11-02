class Solution:
    def maxLen(self, n, l):
        pre = [0]*n
        pre[0] = l[0]
        for i in range(1,n):
            pre[i] = pre[i-1] + l[i]
        pre = [0] + pre
        d = {}
        maxx = 0
        for i in range(n+1):
            x = pre[i]
            if(x not in d):
                d[x] = i
            else:
                maxx = max(maxx,i-d[x])
        return maxx