from typing import List
import time

class Solution1:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Note:
            # input:
                # nums: List[int]
            # output:
                # output: List[int]
            # goal:
                # givien a list of integers nums, return a list of integers output where output[i] is the product of the values except itself
        # edge-case:
            # empty input
                # len(nums) > 2
            # non digit nums[i]
                # nums[i] is an integer
        # General approach:
            # brute-force O(n^2) nested loop:
                # iterate the nums (i = index)
                    # iterate the nums (j = index)
                        # compute product except for nums[j] except when j == i
            # optimal solution (static array and 2 pass):
                # initialize an array with length of nums with default value 1
                # iterate nums from 0
                    # compute product to the left of i
                    # update the product to the initialized array
                # iterate the initialized arr from the end of the list
                    # compute the right product
                    # compute the product of left and right
        
        # 1. brute-force:
        output = []
        product = 1
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    product *= nums[j]
            output.append(product)
            product = 1

        return output

        # 2. static array with 2 pass:
        # Pseudocode:
            # output = []
            # l_product = 1
            # for n in nums:
                # output.append(l_product)
                # l_product *= n
            # r_product = 1
            # for i in range(len(output) - 1, -1, -1):
                # output[i] *= r_product
                # r_product *= nums[i]
            # return output

        output = []
        l_product = r_product = 1
        for n in nums:
            output.append(l_product)
            l_product *= n
        
        for i in range(len(output) - 1, -1, -1):
            output[i] *= r_product
            r_product *= nums[i]

        return output

def productExceptSelf(nums: List[int]) -> List[int]:
    # initialize an empty array to store the right (or the left) product of the item at nth index (right_products)
    # iterate the nums array (from the end of the array if getting right product, starting from 0 if left sum) and append the product to the right (or left) product of the item at current index
    
    # initialize the prev_product to 1 (prev_product)
    # iterate the nums array from 1 (end of the arr - 1 if above steps collected left product)
        # set prev_product to product of itself and value of nums[i-1]
        # compute the product of prev_product and right_products[i], then append the value to the response arr
    
    # solution 1
    # num_length = len(nums)
    # res_arr = []
    # l_product = 1

    # for i in range(num_length):
    #     l_product *= 1 if i <= 0 else nums[i-1]
    #     res_arr.append(l_product)

    # # right_products = []
    # r_product = 1
    # for i in range(num_length-1, -1, -1):
    #     r_product *= 1 if i >= num_length - 1 else nums[i+1]
    #     res_arr[i] *= r_product

    # return res_arr

    # solution 2
    # res_arr = []

    # l_product = 1
    # for i in range(len(nums)):
    #     res_arr.append(l_product)
    #     l_product *= nums[i]

    # r_product = 1
    # for i in range(len(nums) - 1, -1, -1):
    #     res_arr[i] = res_arr[i] * r_product
    #     r_product *= nums[i]

    # return res_arr 

    # solution 3
    res_arr = [1] * len(nums)
    
    for i in range(1, len(nums)):
        res_arr[i] = res_arr[i-1] * nums[i-1]

    print(f"left_prod: {res_arr}")
    
    r_product = 1
    for i in range(len(nums) - 1, -1, -1):
        res_arr[i] = res_arr[i] * r_product
        r_product *= nums[i]

    return res_arr

start_time = time.time()
print(productExceptSelf([1,2,4,6]))
print("--- %s seconds ---" % (time.time() - start_time))