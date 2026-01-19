- forward pass: find a window until all elements in s2 are found as subsequence in s1
- backward pass: from the last index, start going backward till all elements in s2 are tracked back
- this ensures that minimum substring which is subsequence of s2 is found
``` python
class Solution:
    def minWindow(self, s1, s2):
        i,n,m=0,len(s1),len(s2)
        res=""
        while i<n:
            j=0
            r=i
            while r<n:
                if s1[r]==s2[j]: 
                    j+=1
                    if j==m: break
                r+=1
            if j<m: break
            j=m-1
            end=r
            while r>=i:
                if s1[r]==s2[j]:
                    j-=1
                    if j<0: break
                r-=1
            start=r
            if res=="" or len(res)>end-start+1:
                res=s1[start:end+1]
            i=start+1
        return res
