class Solution:
    def canServe(self, arr):
        five,ten=0,0
        for rs in arr:
            if rs==5: five+=1
            if rs==10: 
                if five==0: return False
                five-=1
                ten+=1
            if rs==20:
                if ten>=1 and five>=1:
                    ten-=1
                    five-=1
                elif five>=3:
                    five-=3
                else: return False
        return True
