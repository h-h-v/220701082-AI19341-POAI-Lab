graph = {}
def add_edge(u, v):
    graph.setdefault(u, []).append(v)
    graph.setdefault(v, []).append(u)
def dfs(n, v=set()):
    if n not in v: v.add(n); print(n, end='->2'); [dfs(nei, v) for nei in graph.get(n, [])]
while (e := input("Edge (u v) or 'done'): ")) != 'done':
    add_edge(*map(int, e.split()))
dfs(int(input("Start node: ")))
