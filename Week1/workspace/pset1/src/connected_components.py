# Uses python3

import sys


def number_of_components(adj):
    result = 0
    cc = 1
    ccNum = [cc] * n
    visited = [False] * n
    # print(adj)
    # print(ccNum)
    for v in range(len(adj)):
        if not visited[v]:
            explore(adj, visited, ccNum, cc, v)
            cc += 1

    return max(ccNum)


# def reach(adj, x, y):
#     # write your code here
#     # print(adj)
#     visited = [False] * n
#     visited = explore(adj, visited, x)
#     if visited[y]:
#         return 1
#     return 0

def explore(adj, visited, ccNum, cc, v):
    # global visited
    ccNum[v] = cc
    visited[v] = True

    for w in adj[v]:
        # print(w)
        if not visited[w]:
            explore(adj, visited, ccNum, cc, w)



if __name__ == '__main__':
    file1 = open("03.txt", "r")
    input = file1.read()
    #input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(number_of_components(adj))
