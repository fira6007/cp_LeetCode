class Solution:
    def addDigits(self, num: int) -> int:
        length=len(str(num))
        while length!=1:
            strNum=str(num)
            length=len(str(num))
            num=0
            for x in strNum:
                num+=int(x)
        return num
                