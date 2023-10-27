class Solution:
    def stockBuySell(self, arr, n):
        li=[]
        inv=0
        for i in range(1,n):
            if(arr[i]<arr[i-1]):
                if(inv!=i-1):
                    li.append([inv,i-1])
                inv=i
        if(arr[-1]>arr[-2]):li.append([inv,n-1])
        return li