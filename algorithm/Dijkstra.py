def find_shortest_distances(matrix, start):
    n = len(matrix)
    distances = [float('inf')] * n
    distances[start] = 0
    visited = [False] * n

    for _ in range(n):
        # 遍历，找到未被访问的节点中距离出发点最近的
        min_distance = float('inf')

        for v in range(n):
            if not visited[v] and distances[v] < min_distance:
                min_distance = distances[v]
                u = v

        visited[u] = True  # 将这个节点标记为已经访问过

        # 使用这个选中的节点来更新所有距离
        for v in range(n):
            if matrix[u][v] != -1 and not visited[v]:  # 如果uv是连通的并且v未被访问过
                distances[v] = min(distances[v], distances[u] + matrix[u][v])

    # 再把不可达的点替换回去，不过这时候只有孤立点才会不可达了
    distances = [-1 if d == float('infinity') else d for d in distances]

    return distances


if __name__ == '__main__':
    matrix = [[-1, 3, -1, 7],
              [3, -1, 5, -1],
              [-1, 5, -1, 2],
              [7, -1, 2, -1]]
    start_vertex = 0
    shortest_distances = find_shortest_distances(matrix, start_vertex)
    print(shortest_distances)
