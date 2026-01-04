# similar to Max sliding sum
class Solution:
    def maxSubarraySum(self, arr, k):
        res=cur=0 # cur holds current running sum -  we use 2 pointers to keep track of window size 
        l,n=0,len(arr)
        for r in range(n):
            if r>=k:
                res=max(res,cur)
                cur-=arr[l]
                l+=1
            cur+=arr[r]
        return max(res,cur)
