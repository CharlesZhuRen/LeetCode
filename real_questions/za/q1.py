import sys

def solution(matrix, n, m):
    """
    规则：
    1、*必须是2*2的
    2、*的边和角不能相接
    """
    processed = [[False] * m for _ in range(n)]

    cornors = []

    for i in range(n - 1):
        for j in range(m - 1):
            # 遍历矩阵，找到每一个色块
            if matrix[i][j] == "*" and matrix[i + 1][j] == "*" and matrix[i][j + 1] == "*" and matrix[i + 1][j + 1] == "*":
                # 记录被染色的色块
                processed[i][j] = True
                processed[i + 1][j] = True
                processed[i][j + 1] = True
                processed[i + 1][j + 1] = True
                # 记录被染色色块的左上角，用于标识
                cornors.append((i, j))

    # print(cornors)
    # 没有合法的被染色的2*2的色块
    if len(cornors) == 0:
        return "No"

    for i, j in cornors:
        # print(i, j)
        # 检查被染色的色块是否不和其他色块沾边：
        surroundings = [
            (i - 1, j - 1), (i - 1, j), (i - 1, j + 1), (i - 1, j + 2),
            (i + 2, j - 1), (i + 2, j), (i + 2, j + 1), (i + 2, j + 2),
            (i, j - 1), (i + 1, j - 1),
            (i, j + 2), (i + 1, j + 2)
        ]

        for x, y in surroundings:
            if 0 <= x < n and 0 <= y < m and processed[x][y]:
                return "No"

    return "Yes"


asks = int(input())

for i in range(asks):
    n, m = sys.stdin.readline().split()
    n, m = int(n), int(m)

    matrix = []

    for j in range(n):
        matrix.append(sys.stdin.readline().strip())

    print(solution(matrix, n, m))


