import os


#     A
#   / | \       
#  B  C  D
#   \ | /
#     E
#     |
#     F 

graph = {
    'A': ['B','C','D'],
    'B': ['A','E'],
    'C': ['A','E'],
    'D': ['A','E'],
    'E': ['B','C','D','F'],
    'F': ['E']
}

def dfs(graph,start):
    stack = [start]
    visited = [start]
    while (stack):
        v = stack.pop()
        if v not in path:
            path.append(v)
            visited = visited + graph[v]
            print 'visited: {}'.format(visited)
    return path

def dfs_recursive(graph, start, path=[]):
    path = path + [start]
    for vertex in graph[start]:
        if vertex not in path:
            path=dfs_recursive(graph, vertex, path)
    return path


def dfs_iterative(graph, start):
    stack, path = [start], []

    while stack:
        print 'path_dfs:{}'.format(path)
        print 'stack_dfs:{}'.format(stack)
        vertex = stack.pop()
        # print 'vertex_dfs:{}'.format(vertex)
        if vertex in path:
            continue
        path.append(vertex)
        for neighbor in graph[vertex]:
            stack.append(neighbor)
    return path

def bfs_iterative(graph, start):
    queue, path = [start], []

    while queue:
        # print 'path_bfs:{}'.format(path)
        # print 'queue_bfs:{}'.format(queue)
        vertex = queue.pop(0)
        # print 'vertex_bfs:{}'.format(vertex)
        if vertex in path:
            continue
        path.append(vertex)

        for neighbor in graph[vertex]:
            queue.append(neighbor)
    return path


# dfs_recursive = dfs_recursive(graph,'A')
# print 'dfs_recursive:{}'.format(dfs_recursive)


# dfs_iterative = dfs_iterative(graph,'A')
# print 'dfs_iterative:{}'.format(dfs_iterative)

# bfs_iterative = bfs_iterative(graph,'A')
# print 'bfs_iterative:{}'.format(bfs_iterative)


def dfs_iterative_new(graph, start):
    stack, path = [start], []

    while stack:
        print 'path_dfs:{}'.format(path)
        print 'stack_dfs:{}'.format(stack)
        vertex = stack.pop()
        if vertex in path:
            continue
        path.append(vertex)
        for neighbor in reversed(graph[vertex]):
            if neighbor not in path:
                stack.append(neighbor)
    return path

dfs_iterative_new = dfs_iterative(graph,'A')
print 'dfs_iterative_new:{}'.format(dfs_iterative_new)
