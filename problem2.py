# Q2. Three Sum Problem Sample Problem: Given an array of 
# integers, find all unique triplets in the array which give the sum of 
# zero. The solution should return the list of triplets.  
def three_sum(nums):
    nums.sort()
    triplets = []

    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left, right = i + 1, len(nums) - 1

        while left < right:
            total = nums[i] + nums[left] + nums[right]

            if total < 0:
                left += 1
            elif total > 0:
                right -= 1
            else:
                triplets.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1

    return triplets


# Example usage:
nums = [-1, 0, 1, 2, -1, -4]
result = three_sum(nums)
print("Unique Triplets:", result)
