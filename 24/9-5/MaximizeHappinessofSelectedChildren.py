class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:

        happiness.sort(reverse=True)
        s,n=0,len(happiness)
        for i,j in enumerate(happiness):
            if k!=0:
                s+=j-i if j-i>0 else 0
                k-=1
            else:
                break
        return s