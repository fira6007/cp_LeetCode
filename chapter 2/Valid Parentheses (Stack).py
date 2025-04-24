class Solution:
    def isValid(self, s: str) -> bool:
        a=[]
        char1=['(','{','[']
        char2=[')','}',']']

        for x in range(0,len(s)):
            if s[x] in char1:
            
                a.append(s[x])
            elif s[x] in char2 and len(a)!=0:
                c= char2.index(s[x])
                if a[-1]==char1[c]:
                    a.pop()
                else:
                    return False
            else:
                return False
        if len(a)==0 :
            return True 
        else:
            return False