import math


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def serialize(root: Node) -> str:
    if not root:
        return "None"

    nodes = []
    togo = [root]

    while not all(node is None for node in togo):
        cur = togo.pop(0)

        if cur is None:
            nodes.append(None)
            # togo.append(None) 不注释掉会有错
            # togo.append(None)
        else:
            nodes.append(cur.val)
            togo.append(cur.left)
            togo.append(cur.right)
            # print(cur.val, cur.left, cur.right)

        # print(togo)

    # 做一个补全，如果长度不完全的话，就填充None
    # 对于一个长度完全的res，它的长度+1=2的n次方，因此先判断n+1是否为2的n次方
    # padding以后就好办了，可以分层处理了，但padding也仅仅是用来进行分层的
    n = len(nodes)
    if ((n + 1) & n) != 0:
        to_padd = 2 ** math.ceil(math.log2(n + 1)) - (n + 1)
        # print(to_padd)
        nodes += [None] * to_padd

    return ",".join([str(i) for i in nodes])


def deserialize(nodes: str):
    # 给nodes分层
    # 每一层分别有2**0，2**1，2**2，2**4，2**（m-1）个，m为层数
    nodes = nodes.split(",")

    n = len(nodes)
    l = int(math.log2(n + 1))
    levels = [[nodes[0]]]
    for i in range(1, l):
        this_level = nodes[2 ** (i) - 1:2 ** (i + 1) - 1]
        levels.append(this_level)

    # print(levels)

    # 对每一层进行构建
    # 可能从下往上构建好点，这样最后就直接返回root
    # 对于第i层里的j节点
    # 它的左子节点=第i+1层的第j*2个节点
    # 它的右子节点=第i+1层的第j*2+1个节点
    levels = levels[::-1]
    # print(levels)
    # val构建为节点
    levels = [[Node(i) for i in level] for level in levels]
    # print([[i.val for i in level] for level in levels])

    for i in range(l - 1):
        n_level = len(levels[i + 1])

        for j in range(n_level):
            levels[i + 1][j].left = levels[i][j * 2]
            levels[i + 1][j].right = levels[i][j * 2 + 1]

    return levels[-1][0]


def test(root):
    res = serialize(root)
    print(res)
    root = deserialize(res)
    res = serialize(root)
    print(res)
    root = deserialize(res)
    res = serialize(root)
    print(res)
    print()


if __name__ == '__main__':
    # case 1
    root = Node(5, left=Node(2, left=Node(1)), right=Node(4, left=Node(3)))
    test(root)

    # case 2
    # root = Node(1)

    # case 3
    # root = Node(1, left=Node(2))

    # case 4
    # root = Node(1, left=None, right=Node(2))

    # case 5
    root = Node(1, left=Node(2), right=Node(3, left=Node(4), right=Node(5)))
    test(root)
