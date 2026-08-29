class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        count = {}
        res, maxCount = 0,0

        for val in nums:
            count[val] = 1+ count.get(val,0)
            res = val if count[val]>maxCount else res
            maxCount = max(count[val],maxCount)
        return res

    
