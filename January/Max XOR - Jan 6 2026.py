class Solution:
    def maxSubarrayXOR(self, arr, k):
        res,cur,l,n=0,0,0,len(arr)
        for r in range(n):
            cur^=arr[r]
            if r-l+1==k: 
                res=max(res,cur)
                cur^=arr[l] #removes arr[l]
                l+=1
        return res
