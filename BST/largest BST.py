
class Solution:
    
    def largestBst(self, root):
        
        a=-10**9
        b=10**9
        ans=-1
        
        def solve(root):
            nonlocal ans
            if root==None:
                return [0,True,a,b]    ###size,valid,max_val,min_val
                
            lef=solve(root.left)
            rig=solve(root.right)
            
            if lef[1] and rig[1] and root.data>lef[2] and root.data<rig[3]:
                ans=max(ans,1+lef[0]+rig[0])
                return[1+lef[0]+rig[0],True,max(root.data,rig[2]),min(root.data,lef[3])]
                
            return[1,False,root.data,root.data]
                
        solve(root)
        return ans
            
        
            
        
            