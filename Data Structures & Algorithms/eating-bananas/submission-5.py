class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        while low<high:
            count = 0
            mid = (low+high)//2
            for i in piles:
                count += (i + mid - 1) // mid
            if count<=h:
                high = mid
            else:
                low = mid+1
        return low
    
