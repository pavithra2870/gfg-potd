  * `rep`: frequency map of elements in the current window.
  * `dis`: set of distinct elements in the current window.
* Expand the window by moving `r`:

  * Add `arr[r]` to `rep`.
  * If it’s new, also add it to `dis`.
* When window size reaches `k`:

  * Number of distinct elements = `len(dis)`, store it.
* Slide the window forward by moving `l`:

  * Decrease count of `arr[l]` in `rep`.
  * If its count becomes `0`, remove it from `dis`.

```python
class Solution:
    def countDistinct(self, arr, k):
        dis,rep=set(),{}
        l,res,n=0,[],len(arr)
        for r in range(n):
            if rep.get(arr[r],0)>0: rep[arr[r]]+=1
            else: 
                dis.add(arr[r])
                rep[arr[r]]=1
            if r>=k-1:
                res.append(len(dis))
                rep[arr[l]]-=1
                if rep[arr[l]]==0: dis.remove(arr[l])
                l+=1
        return res
```
