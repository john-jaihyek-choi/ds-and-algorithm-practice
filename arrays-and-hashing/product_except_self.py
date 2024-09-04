from typing import List
import time

def productExceptSelf(nums: List[int]) -> List[int]:
    # initialize an empty array to store the right (or the left) product of the item at nth index (right_products)
    # iterate the nums array (from the end of the array if getting right product, starting from 0 if left sum) and append the product to the right (or left) product of the item at current index
    
    # initialize the prev_product to 1 (prev_product)
    # iterate the nums array from 1 (end of the arr - 1 if above steps collected left product)
        # set prev_product to product of itself and value of nums[i-1]
        # compute the product of prev_product and right_products[i], then append the value to the response arr
    
    num_length = len(nums)
    res_arr = []
    l_product = 1

    for i in range(num_length):
        l_product *= 1 if i <= 0 else nums[i-1]
        res_arr.append(l_product)

    # right_products = []
    r_product = 1
    for i in range(num_length-1, -1, -1):
        r_product *= 1 if i >= num_length - 1 else nums[i+1]
        res_arr[i] *= r_product

    return res_arr

start_time = time.time()
print(productExceptSelf([1,2,4,6]))
print("--- %s seconds ---" % (time.time() - start_time))