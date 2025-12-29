s = [1, 2, 3, 4, 5, 7]
target = 20
def binary_search(s, target):
    low = 0
    high = len(s) - 1
    while low <= high:
        mid = (low + high) // 2
        if s[mid] == target:
            return "found"
        elif s[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    return "not found"
print(binary_search(s, target))
