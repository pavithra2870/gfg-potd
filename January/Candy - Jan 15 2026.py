class Solution:
    def minCandy(self, arr):
        n=len(arr)
        c=[1]*n
        for i in range(1,n):
            if arr[i]>arr[i-1]: c[i]=1+c[i-1]
        for i in range(n-2,-1,-1):
            if arr[i+1]<arr[i] and c[i]<=c[i+1]: c[i]=c[i+1]+1
        return sum(c)
