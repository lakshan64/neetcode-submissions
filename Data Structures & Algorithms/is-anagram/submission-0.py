class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        i=list(s)
        j=list(t)
        i.sort()
        j.sort()
        if i == j:
            return True
        else:
            return False
