"""
核心：哨兵划分
- 选择数组中的某个元素作为基准数（这里是每次选择数组最左侧的数）
- 将所有小于基准数的元素移到基准数的左侧
- 将所有大于基准数的元素移到基准数的右侧
"""


def partition(nums: list[int], left: int, right: int) -> int:
    i, j = left, right
    # 每次从左侧找到第一个比基准数大的数，从右侧找到第一个比基准数小的数，交换这两个数
    # 一直交换，知道i和j相遇为止
    while i < j:
        while i < j and nums[j] >= nums[left]:
            j -= 1
        while i < j and nums[i] <= nums[left]:
            i += 1

        nums[i], nums[j] = nums[j], nums[i]
    # 此时下标从0到i的数都是<=pivot，从i+1到right的数都是>pivot
    # 交换第i个数和位于left位置的pivot
    # 此时pivot就处于正确的位置上了，也就是这个数组被pivot正确的划分了，返回pivot的下标即可
    nums[i], nums[left] = nums[left], nums[i]
    return i


def quick_sort(nums: list[int], left: int, right: int):
    if left >= right:
        return

    pivot = partition(nums, left, right)

    # TODO: 尾递归优化
    quick_sort(nums, left, pivot - 1)
    quick_sort(nums, pivot + 1, right)


if __name__ == '__main__':
    a = [7, 6, 5, 1, 3, 2, 4, 9, 8]
    quick_sort(a, 0, len(a) - 1)
    print(a)
