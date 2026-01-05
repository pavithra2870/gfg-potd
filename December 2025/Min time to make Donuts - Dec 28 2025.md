# Minimum time to fulfil all orders
- Find the smallest X such that f(X) is true -> Binary Search
- Monotonic means: Once a value works, all bigger values also work
- If I guess an answer X, can I check in O(n) whether X is valid, and does validity change monotonically?
- we do binary search on time to find minimum time in which given chefs can make n donuts
- use quadratic formula to find how many donuts a chef of rank r can make in time t as r*k*(k+1)/2 <= t
  
<img width="747" height="311" alt="image" src="https://github.com/user-attachments/assets/8e3f942d-4cd0-4319-997d-b732dfb1728b" />

```python
class Solution:
    def minTime(self, ranks, n):
        from math import sqrt
        def donuts(r,t):
            d=1.0+(8.0*t/r)
            return int((sqrt(d)-1)/2.0)
        def canMake(t):
            d=0
            for r in ranks:
                d+=donuts(r,t) 
                if d>=n: return True
            return d>=n
        l,h,res=0,min(ranks)*n*(n+1)//2,0
        while l<=h:
            m=(l+h)//2
            if canMake(m):
                res=m
                h=m-1
            else: l=m+1
        return res
```
