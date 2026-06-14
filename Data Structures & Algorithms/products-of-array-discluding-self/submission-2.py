class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """products = []
        for i in range(len(nums)):
            products.append(1)
            for j in range(len(nums)):
                if i==j: continue 
                products[i]*=nums[j]
        return products"""
        product_carry=1
        products=[1]*len(nums)
        for i in range(1, len(nums)):
            product_carry*=nums[i-1]
            products[i] *= product_carry
        product_carry=1
        for j in range(len(nums)-2, -1, -1):
            product_carry*=nums[j+1]
            products[j] *= product_carry
        return products