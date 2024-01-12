class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        n = len(gas)
        sum = 0  # 油箱中油的数量
        min = 0  # 从起点出发 油箱中油量的最小值
        idx = 0
        for i in range(n):
            sum += gas[i] - cost[i]
            if sum < min:
                # 如果剩余油量比最小值小, 更新这个最小值, 并将起点置为当前点后面一个点
                # 最开始的时候min是0 比0还小那说明怎么都走不到这里, 那就直接面向未来, 换个新起点, 之后<min也是同理
                min = sum
                idx = i + 1

        if sum < 0:  # 遍历一圈之后如果不剩油了 说明走不了一圈
            return -1
        else:  # 否则返回正确起点
            return idx
