class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        products = []
        print(nums)
        for i, el in enumerate(nums):
            product = 1
            for j, el2 in enumerate(nums):
                if i==j: continue
                product*=el2
            print(product)
            products.append(product)
        return products