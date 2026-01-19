- we use monotonic decreasing queue - end of queue shud be greater than current element
- we first clean end of queue - ensure that last element is always greather than current element
- we next clean start of queue - to discard indices that are out of window bounds (index < l)
- then we push current element into queue
- first element of queue is the max element in current window so append it in res and incremenet left
```python
class Solution:
    def maxOfSubarrays(self, arr, k):
        if k==1: return arr
        q=deque()
        res=[]
        l=0
        n=len(arr)
        for r in range(n):
            while q and arr[q[-1]]<arr[r]: q.pop()
            while q and q[0]<l: q.popleft()
            q.append(r)
            if r>=k-1:
                res.append(arr[q[0]])
                l+=1
        return res
