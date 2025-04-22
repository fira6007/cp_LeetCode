import math
class Solution:
    def reverse(self, x: int) -> int:
        if not x> math.pow(2,31) -1 and not x< math.pow(-2,31):
            if x>0 :
                z=int(str(x)[::-1])
                if z > math.pow(2,31) -1 :
                    return 0
                else:
                    return z
            else:
                z= int("-"+str(x* (-1))[::-1])
                if z < math.pow(-2,31):
                    return 0
                else:
                    return z