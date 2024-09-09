"""
题目描述：
现有一个狭小的老鼠洞，每次仅能一只老鼠进或者出（类似于栈的特性），如果通道里有多只老鼠，那么先进洞的老鼠会
比晚进洞的老鼠出来更晚，假如有一窝老鼠来串门，我们给每只老鼠单独编个数字号码，1、2、3
允许老鼠进洞后，又出洞，再次进洞，且若众多老鼠都挤满到洞门口了，则不会再有老鼠进洞，最后出洞的顺序就按洞
口到洞底的老鼠编号输出。假如老鼠进洞的顺序是1、2、3，那么可能的出洞顺序是3、2、1，考虑到洞未满的情况
下，老鼠进洞后又出洞了，也可能是1、2、3等，但不可能是3、1、2。
现给定一个进洞序列，序列里数字可能重复，重复表示出洞后再次进洞，假定序列最后洞是满的，序列长度小于10000
，即老鼠编号范国是（1,10000」
请给出老鼠出洞的顺序？

输入描述：
输入一行数字数列，每个数字之间用英文空格分隔。如123

输出描述：
321
"""


def solution(in_sequence: str):
    in_sequence = list(in_sequence.split(" "))

    stack = []  # 用栈模拟洞
    result = []
    pos_map = {}  # 记录老鼠在洞中的位置

    for mouse in in_sequence:
        if mouse in pos_map:  # 如果老鼠已经在栈中
            # 弹出栈顶元素，直到弹出该老鼠，并把他们都加入到result里，然后更新pos_map
            while len(stack) > pos_map[mouse]:
                popped_mouse = stack.pop()
                result.append(popped_mouse)
                del pos_map[popped_mouse]  # 更新哈希表
        else:
            # 将老鼠入栈并记录位置
            stack.append(mouse)
            pos_map[mouse] = len(stack) - 1

    # 最后将栈中的元素弹出并加入结果
    while stack:
        result.append(stack.pop())

    return " ".join(map(str, result))


if __name__ == '__main__':
    in_seq = "1 2 3 3 2 1"
    print(solution(in_sequence=in_seq))
