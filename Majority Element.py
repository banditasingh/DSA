class Solution:
    def majorityElement(self, a, n):
        if n==1:
            return a[0]
        if n==2:
            if a[0]==a[1]:
                return a[0]
            return -1
        d=dict.fromkeys(set(a),0)
        for i in a:
            d[i]+=1
        a=list(set(a))
        for i in a:
            if d[i]>=n//2+1:
                return i
        return -1