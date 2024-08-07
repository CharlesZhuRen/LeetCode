class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        # 非递减: 后一个元素>=前一个元素

        # 方法一: 先合并后排序
        # nums1[m:] = nums2
        # nums1.sort()

        # 方法二: 双指针
        # sorted = []  # 不过这里需要创建一个新的数组, 使用了额外的存储空间
        # p1, p2 = 0, 0
        # while p1 < m or p2 < n:  # 其中有一个没遍历完
        #     if p1 == m:  # nums1已经遍历完毕, 只需要逐个加入nums2即可
        #         sorted.append(nums2[p2])
        #         p2 += 1
        #     elif p2 == n:  # 同理
        #         sorted.append(nums1[p1])
        #         p1 += 1
        #     elif nums1[p1] < nums2[p2]:  # 把小的那个加进去, 保证非递减
        #         sorted.append(nums1[p1])
        #         p1 += 1
        #     else:
        #         sorted.append(nums2[p2])
        #         p2 += 1
        #
        # # 更新原数组
        # nums1[:] = sorted

        # 方法三: 逆向双指针, 避免覆盖原数组, 不用创建新数组
        # p1, p2 = m - 1, n - 1  # nums1和nums2的指针
        # tail = m + n - 1  # nums1的尾指针
        # while p1 >= 0 or p2 >= 0:
        #     if p1 == -1:
        #         nums1[tail] = nums2[p2]
        #         p2 -= 1
        #     elif p2 == -1:
        #         nums1[tail] = nums1[p1]
        #         p1 -= 1
        #     elif nums1[p1] > nums2[p2]:
        #         nums1[tail] = nums1[p1]
        #         p1 -= 1
        #     else:
        #         nums1[tail] = nums2[p2]
        #         p2 -= 1
        #     tail -= 1

        # 方法三优化
        p1 = m - 1  # 从后往前移动，指向nums1中的实值
        p2 = n - 1  # 从后往前移动，指向nums2中的实质
        p3 = m + n - 1  # 从后往前移动，指向nums1需要被赋值的位置
        while p1 >= 0 and p2 >= 0:  # 有任何一个为-1，说明已经遍历完其中一个，应跳出循环
            if nums1[p1] > nums2[p2]:  # 移动num1到nums1尾部
                nums1[p3] = nums1[p1]
                p1 -= 1
            else:
                nums1[p3] = nums2[p2]
                p2 -= 1

            p3 -= 1

        if p1 == -1:  # nums1先遍历结束，把nums2剩余的放到nums1的前面
            nums1[:p2 + 1] = nums2[:p2 + 1]
