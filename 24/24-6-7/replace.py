class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        ans=""
        value=sentence.split(" ")
        for i in value:
            r,l="",101
            for j in dictionary:
                if i.startswith(j) and len(j)<l:
                        r=j
                        l=len(j)
            if r=="":
                ans+=i+" "
            else:
                ans+=r+" "
        return ans[:-1]
                