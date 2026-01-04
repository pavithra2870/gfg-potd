# Sort 0s, 1s and 2s in 0(n) - classic Dutch National Flag 

- indices 0 to low-1 contains all 0s
- low to mid-1 contains all 1s
- mid to high contains all 2s

1. iterate array through mid ptr as long as mid<=high
2. if mid element is 1, it is already in correct position so just increase mid ptr by 1
3. if mid element is 0, we swap it with element in low ptr and we increase both ptrs by 1 to expand the 0 and 1 sections
4. if mid element is 2, we swap it with element in high ptr and we only decrease high ptr by 1 because the element that was swapped from high position should be checked once

```python3 []
class Solution:
    def sort012(self, arr):
        l,m,h=0,0,len(arr)-1
        while m<=h:
            e=arr[m]
            if e==0:
                arr[m],arr[l]=arr[l],arr[m]
                m+=1
                l+=1
            if e==1:
                m+=1
            if e==2:
                arr[h],arr[m]=arr[m],arr[h]
                h-=1
        return arr
```
