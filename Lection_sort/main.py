# быстрая сортировка


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]
        great = [i for i in arr[1:] if i > pivot]
    return quick_sort(less) + [pivot] + quick_sort(great)


print(quick_sort([23, -5, 89, 0, 1, 5, -3]))


# сортировка слиянием


def merge_sort(nums):
    if len(nums) > 1:
        mid = len(nums) // 2
        left = nums[:mid]
        right = nums[mid:]
        merge_sort(left)
        merge_sort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            nums[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            nums[k] = right[j]
            j += 1
            k += 1


nums = [38, 27, 43, 3, 9, 82, 10]
merge_sort(nums)
print(nums)
