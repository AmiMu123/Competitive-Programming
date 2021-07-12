class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dic_s = dict()
        dic_t = dict()
                
        for i in range(len(s)):
            char_s = s[i]
            char_t = t[i]
            
            if char_s not in dic_s:
                dic_s[char_s] = char_t
            if char_t not in dic_t:
                dic_t[char_t] = char_s
            if dic_t[char_t] != char_s or dic_s[char_s]  != char_t:
                return False
        return True
            
                
            
        
