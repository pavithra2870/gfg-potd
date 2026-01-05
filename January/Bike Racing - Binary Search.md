# Find the minimum number of hours after which the safety alarm will start.

- binary search on hours
- if sum of all speeds of fast riders for a given hour is >= maxx, it is a possible solution so we will search for a lesser hour

```python
class Solution:
	def buzzTime(self,n,maxx,l,h,a):
	    def canCross(m):
	        tot=0
	        for i in range(n):
	            sp=h[i]+a[i]*m
	            if sp>=l: tot+=sp
	            if tot>=maxx: return True
	        return False
	    lo,hi,res=1,10**18,0
	    while lo<=hi:
	        m=(lo+hi)//2
	        if canCross(m):
	            res=m
	            hi=m-1
	        else: lo=m+1
	    return res
