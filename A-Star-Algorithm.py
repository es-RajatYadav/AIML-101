def aStar(startNode, stopNode):
    openSet = set(startNode)
    closedSet = set()
    g = {startNode: 0}
    parents = {startNode: startNode}

    while len(openSet) > 0:
        n = None
        for v in openSet:
            if n is None or g[v] + heu(v) < g[n] + heu(n):
                n = v
        if n == stopNode or graphNodes[n] is None:
            pass
        else:
            for (m, weight) in getNeighbors(n):
                if m not in closedSet and m not in openSet:
                    openSet.add(m)
                    parents[m] = n
                    g[m] = g[n] + weight
                else:
                    if g[m] > g[n] + weight:
                        parents[m] = n
                        g[m] = g[n] + weight
                        if m in closedSet:
                            openSet.add(m)
                            closedSet.remove(m)
        if n is None:
            print("Path doesn't exists!!")
            return None

        if n == stopNode:
            path = []
            while parents[n] != n:
                path.append(n)
                n = parents[n]
            path.append(startNode)
            path.reverse()
            print("Path : {}".format(path))
            return path
        closedSet.add(n)
        openSet.remove(n)
    print("Path doesn't exist!!")
    return None


def getNeighbors(v):
    if v in graphNodes:
        return graphNodes[v]
    else:
        return None


def heu(n):
    H_dist = {
        'A': 5,
        'B': 6,
        'C': 7,
        'D': 0,
    }
    return H_dist[n]


graphNodes = {
    'A': [('B', 6), ('C', 8)],
    'B': [('D', 6)],
    'C': [('D', 8)]
}

aStar('A', 'D')
