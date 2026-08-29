class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        for char in s:
            res = t.find(char)
            if(res == -1):
                return False;    
            t = t.replace(char,'',1)

        return True;
            
