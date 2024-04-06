class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # new = dict() # key=num, value=[index]
        # for i, num in enumerate(nums):
        #     if new.get(num):
        #         new[num].append(i)
        #     else:
        #         new[num] = [i]

        # for num in new.keys():
        #     if len(new[num]) > 1:
        #         for i in new[num]:
        #             for j in new[num]:
        #                 if abs(i - j) <= k and i != j:
        #                     return True

        # return False

        pos = {}  # key=num, value=previous position，一次遍历即可
        for i, num in enumerate(nums):
            if num in pos and i - pos[num] <= k:
                return True
            pos[num] = i
        return False
