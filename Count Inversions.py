class Solution:
    
    def merge(self,arr, left, mid, right):
        i=left
        j=mid+1
        temp = list()
        inv = 0
        while i<=mid and j<=right:
            if arr[i]<=arr[j]:
                temp.append(arr[i])
                i=i+1
            else:
                temp.append(arr[j])
                j=j+1
                inv = inv+(mid-i+1)
        
        while i<=mid:
            temp.append(arr[i])
            i = i+1
        while j<=right:
            temp.append(arr[j])
            j=j+1
        

        for i in range(len(temp)):
            arr[left + i] = temp[i]
        return inv
    
    
    def mergesort(self,arr, left, right):
        inv = 0
        if left<right:
            mid = (right+left)//2
            inv = inv+self.mergesort(arr,left, mid)
            inv=inv+self.mergesort(arr, mid+1, right)
            inv = inv+self.merge(arr, left, mid, right)
        return inv


    def inversionCount(self, arr, n):
        left = 0
        right = n-1
        return self.mergesort(arr, left, right)