class Solution:
    def search(self, nums: List[int], target: int) -> int:
        try:
            n=nums.index(target)
            return n
        except:
            return -1