class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        res,count = 0,0
        for n in nums:
            if count == 0:
                res = n
            count += (1 if n==res else -1)
        return res


        # count = {}
        # res, maxCount = 0,0

        # for val in nums:
        #     count[val] = 1+ count.get(val,0)
        #     res = val if count[val]>maxCount else res
        #     maxCount = max(count[val],maxCount)
        # return res

    
