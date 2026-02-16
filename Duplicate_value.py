#Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
nums = [1, 2, 3, 1]
found_duplicate = False

for i in range(len(nums) - 1):
    for j in range(i + 1, len(nums)):
        if nums[i] == nums[j]:
            found_duplicate = True
            break 
    if found_duplicate:
        break 

if found_duplicate:
    print("True")
else:
    print("False")
#optimized Soln using set
my_set = set(nums)
result = len(nums) != len(my_set)
print(result)

   



