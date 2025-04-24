class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        count=0
        for x in sentences:
            words=x.split(" ")
            if len(words)>count:
                count=  len(words)
        return count