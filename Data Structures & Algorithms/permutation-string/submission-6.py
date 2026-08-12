class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        r = len(s1)
        freq1 = [0]*26
        for i in s1:
            freq1[ord(i)-ord('a')]+=1
        freq2 = [0]*26
        print(freq1)
        while r<=(len(s2)):
            for i in range(l,r):
                freq2[ord(s2[i])-ord('a')]+=1
            if freq1==freq2:
                return True
            print(freq2)
            l+=1
            r+=1
            freq2 = [0]*26
        return False