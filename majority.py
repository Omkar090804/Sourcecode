def find_majority_element(nums):
   
    candidate = None
    count = 0
    
    for num in nums:
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1)
    
    if nums.count(candidate) > len(nums) // 2:
        return candidate
    else:
        return None

nums = [2, 2, 1, 1, 1, 2, 2]
result = find_majority_element(nums)

if result:
    print("Majority Element:", result)
else:
    print("No Majority Element found")
