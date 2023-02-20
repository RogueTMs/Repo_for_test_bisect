def search(nums, target: int) -> int:
    l = 0
    r = len(nums) - 1

    while l <= r:
        cur = (l + r) // 2
        if nums[cur] == target:
            return cur
        elif nums[cur] > target:
            r = cur - 1
        else:
            l = cur + 1

    return False


nums = [-1, 0, 3, 5, 9, 12]
target = 9

ans = search(nums, target)
assert ans == 4, 'Упал'

nums = [-1, 0, 3, 5, 9, 12]
target = 2

ans = search(nums, target)
assert ans == -1, 'Упал'