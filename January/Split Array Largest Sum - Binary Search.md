- Divide the array into k contiguous subarrays such that the maximum sum among these subarrays is minimized.
- Find this minimum possible maximum sum.
- same as painters partition
- binary search on max allowed sum for each subarray
- if we can partition the array into subarrays such that each subarray's sum is <= m, it is a feasible solution. so we need to search for lower sum

```python
class Solution:
    def splitArray(self, arr, k):
        def canSplit(m): #check if every subarray has total sum <=m
            no=1
            cur=0
            for num in arr:
                if cur+num<=m: cur+=num
                else:
                    no+=1
                    cur=num
                if no>k: return False
            return True
        l,r,res=max(arr),sum(arr),0
        while l<=r:
            m=(l+r)//2
            if canSplit(m):
                res=m
                r=m-1
            else: l=m+1
        return res
