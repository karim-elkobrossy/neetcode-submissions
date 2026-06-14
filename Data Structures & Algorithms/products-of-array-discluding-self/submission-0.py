class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        products = []
        for i in range(len(nums)):
            products.append(1)
            for j in range(len(nums)):
                if i==j: continue 
                products[i]*=nums[j]
        return products
