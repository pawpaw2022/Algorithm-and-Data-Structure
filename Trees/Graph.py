""" WARNING! This page should not be run as it only shows you the general idea """
# 2 generally used searching algorithms in Graph.

# Depth First Search (DFS) Example

# DFS recursively
marked = [False] * G.size()
def dfs(G,v):
    visit(v)
    marked[v] = True
    for w in G.neighbors(v):
        if not marked[w]:marked = [False] * G.size()
def dfs(G,v):
            dfs(G, w)
            
# DFS iteratively (Using stack)
marked = [False] * G.size()
def dfs_iter(G,v):
    stack = [v]
    while len(stack) > 0:
        v = stack.pop()
        if not marked[v]:
            visit(v)
            marked[v] = True
            for w in G.neighbors(v):
                if not marked[w]:
                    stack.append(w)

# Breath First Search (BFS) Example

# BFS (Using queue)
marked = [False] * G.size()
def bfs(G, v):
    queue = [v]
    while len(queue) > 0:
        v = queue.pop()
        if not marked[v]:
            visit(v)
            marked[v] = True
            for w in G.neighbors(v):
                if not marked[w]:
                    queue.append(w)

