class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []

        for n in range(numRows):
            rows =[1]
            val = 1
            for k in range(1,n+1):
                val = val*(n-k+1)//k
                rows.append(val)
            res.append(rows)
        return res