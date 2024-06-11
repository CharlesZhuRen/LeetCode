# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""

        nodes = []
        togo = [root]

        while not all(node is None for node in togo):
            cur = togo.pop(0)

            if cur is None:
                nodes.append(None)
                # togo.append(None)
                # togo.append(None)
            else:
                nodes.append(cur.val)
                togo.append(cur.left)
                togo.append(cur.right)

        n = len(nodes)
        if ((n + 1) & n) != 0:
            to_padd = 2 ** math.ceil(math.log2(n + 1)) - (n + 1)
            nodes += [None] * to_padd

        return ",".join([str(i) for i in nodes]).replace("None", "null")

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if data == "":
            return None

        nodes = data.split(",")

        n = len(nodes)
        l = int(math.log2(n + 1))
        levels = [[nodes[0]]]
        for i in range(1, l):
            this_level = nodes[2 ** (i) - 1:2 ** (i + 1) - 1]
            levels.append(this_level)

        levels = levels[::-1]
        levels = [[TreeNode(i) for i in level] for level in levels]

        for i in range(l - 1):
            n_level = len(levels[i + 1])

            for j in range(n_level):
                levels[i + 1][j].left = levels[i][j * 2]
                levels[i + 1][j].right = levels[i][j * 2 + 1]

        return levels[-1][0]

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))