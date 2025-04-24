class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        Sn1=set(nums1)
        Sn2=set(nums2)
        unique=list(Sn1.intersection(Sn2))
        final=[]
        for x in unique:
            if nums1.count(x)>=1 and nums2.count(x)>=1:
                if nums1.count(x)< nums2.count(x):
                    for y in range(0,nums1.count(x)):
                        final.append(x)
                elif nums1.count(x) >= nums2.count(x):
                    for y in range(0,nums2.count(x)):
                        final.append(x)
                else :
                    final.append(x)

        return final