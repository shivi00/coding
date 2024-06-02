class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l,r=0,len(people)-1
        c=0
        while l<=r:
            r-=1
            c+=1 
            if l<=r and limit-people[r+1]>=people[l]:
                l+=1
        return c