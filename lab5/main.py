INF = float('inf')

def prim_mst(vertices, matrix):
    n = len(vertices)
    selected = [False] * n
    selected[0] = True
    mst_edges = []
    total_weight = 0

    print("Хід виконання алгоритму Пріма")
    print(f"{'Ребро':<10} | {'Вага':<6}")
    print("-" * 20)

    for _ in range(n - 1):
        min_weight = INF
        u_idx, v_idx = -1, -1
        for i in range(n):
            if selected[i]:
                for j in range(n):
                    if not selected[j] and matrix[i][j] < min_weight:
                        min_weight = matrix[i][j]
                        u_idx, v_idx = i, j
        selected[v_idx] = True
        mst_edges.append((vertices[u_idx], vertices[v_idx], min_weight))
        total_weight += min_weight
        print(f"{vertices[u_idx]} - {vertices[v_idx]:<6} | {min_weight:<6}")

    print("-" * 20)
    print(f"Загальна вартість МКД (Прім): {total_weight}\n")
    return mst_edges, total_weight


class DisjointSetUnion:
    def __init__(self, elements):
        self.parent = {elem: elem for elem in elements}

    def find(self, i):
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u != root_v:
            self.parent[root_u] = root_v
            return True
        return False


def kruskal_mst(vertices, edges):
    sorted_edges = sorted(edges, key=lambda item: item[2])
    dsu = DisjointSetUnion(vertices)
    mst_edges = []
    total_weight = 0

    print("Хід виконання алгоритму Крускала")
    print(f"{'Ребро':<10} | {'Вага':<6}")
    print("-" * 20)

    for u, v, weight in sorted_edges:
        if dsu.find(u) != dsu.find(v):
            dsu.union(u, v)
            mst_edges.append((u, v, weight))
            total_weight += weight
            print(f"{u} - {v:<6} | {weight:<6}")
            if len(mst_edges) == len(vertices) - 1:
                break

    print("-" * 20)
    print(f"Загальна вартість МКД (Крускал): {total_weight}\n")
    return mst_edges, total_weight


if __name__ == '__main__':
    nodes = [1, 2, 3, 4, 5, 6, 7, 8]
    graph_edges = [
        (1, 3, 2), (1, 4, 4), (1, 2, 8),
        (2, 6, 3), (2, 5, 6),
        (3, 8, 4), (3, 4, 6), (3, 6, 7),
        (4, 5, 1),
        (5, 7, 4),
        (6, 7, 3),
        (7, 8, 5)
    ]

    size = len(nodes)
    node_to_idx = {val: i for i, val in enumerate(nodes)}
    adj_matrix = [[INF] * size for _ in range(size)]
    for i in range(size):
        adj_matrix[i][i] = 0
    for u, v, w in graph_edges:
        i, j = node_to_idx[u], node_to_idx[v]
        adj_matrix[i][j] = w
        adj_matrix[j][i] = w

    prim_mst(nodes, adj_matrix)
    kruskal_mst(nodes, graph_edges)
