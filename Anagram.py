class Solution:
    
    def isAnagram(self,a,b):
        list1 = list(a)
        list2 = list(b)
        list1.sort()
        list2.sort()
        
        string1 = ''.join(list1)
        string2 = ''.join(list2)
        
        if string1 == string2:
            return 1
        else:
            return 0
