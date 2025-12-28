def subsett(nums, subset, i):
    if i == len(nums):
        print(subset)
        return
    subsett(nums, subset, i + 1)
    subset.append(nums[i])
    subsett(nums, subset, i + 1)
    subset.pop()
subsett([1, 2, 3], [], 0)
