class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        #digits = [1,2,3,4,5,6,7,89]
        nums  = 0

        for i in digits:
            nums = 10*nums + i

        nums+=1

        nums = str(nums)
        c = []
        for i in nums:
            c.append(int(i))
        return c

