def dfs(graph, node, visited):
    visited.add(node)
    for neighbor in graph[node]:
        # 遍历当前节点的邻居节点，如果邻居节点未被遍历到，那么调用dfs去遍历它
        if neighbor not in visited:
            dfs(graph, neighbor, visited)


def is_connected(graph):
    if not graph:
        return True

    visited = set()
    start_node = list(graph.keys())[0]  # start from any of the nodes
    dfs(graph, start_node, visited)

    # 如果所有节点都能被遍历到，那么证明是连通图
    return len(visited) == len(graph)


if __name__ == '__main__':
    graph = {
        0: [1, 2],
        1: [0, 2],
        2: [0, 1, 3],
        3: [2]
    }

    print(is_connected(graph))
