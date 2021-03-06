#Uses python3

import sys

sys.setrecursionlimit(200000)


def number_of_strongly_connected_components(adj, adjRev):
    result = 0
    #write your code here
    return result

if __name__ == '__main__':
    file1 = open("02.txt", "r")
    input = file1.read()
    #input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    adjRev = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    for (a, b) in edges:
        adjRev[b - 1].append(a - 1)
    print(adj)
    print(adjRev)
    print(number_of_strongly_connected_components(adj, adjRev))
