# using this list [100, 200, 300] i want to obtain all the posibles permutations of this numbers

def permute(nums):
    if len(nums) == 1:
        return [nums]
    perms = []
    for i in range(len(nums)):
        for perm in permute(nums[:i] + nums[i+1:]):
            perms.append([nums[i]] + perm)
    return perms

print(permute([100, 200, 300]))

# create a function that receives a list of numbers and returns the maximum number in the list 
# 
