
class Solution:
    def minJumps(self, arr, n):
        jump=1
        des=arr[0]
        pos=arr[0]
        if arr[0]==0:
            return -1
        if n<=1:
            return 0
        for i in range(1,n):
            if i==n-1:
                return jump
            des=max(des,i+arr[i])
            pos-=1
            if pos==0:
                jump+=1
                if i>=des:
                    return -1
                pos=des-i
        return -1