distances = [0]

adjacencyList = [[0, 2, 6, 0, 0, 0, 0], [2, 0, 0, 5, 0, 0, 0], [6, 0, 0, 8, 0, 0, 0],
[0, 5, 8, 0, 10, 15, 0], [0, 0, 0, 10, 0, 6, 2], [0, 0, 0, 15, 6, 0, 6], [0, 0, 0, 0, 2, 6, 0]]

unvisitedNodes = [1, 2, 3, 4, 5, 6]

currentNodes = [0]

while len(unvisitedNodes) > 0:
    smallestDistance = ""
    nearestNode = ""
    removeNodes = [True] * len(currentNodes)
    for node in currentNodes :
        for value in adjacencyList[node]:
            adjacentNode = adjacencyList[node].index(value)
            if value > 0:
                if len(distances) >= adjacentNode + 1:
                    if distances[adjacentNode] > distances[node] + value:
                        distances[adjacentNode] = distances[node] + value
                else:
                    distances.append(distances[node] + value)
                if adjacentNode in unvisitedNodes:
                    removeNodes[currentNodes.index(node)] = False
                    if smallestDistance == "":
                        smallestDistance = distances[adjacentNode]
                        nearestNode = adjacentNode
                    if distances[adjacentNode] < smallestDistance:
                        smallestDistance = distances[adjacentNode]
                        nearestNode = adjacentNode

    unvisitedNodes.remove(nearestNode)
    currentNodes.append(nearestNode)

    nodeValues = []
    index = 0
    for node in removeNodes:
        if node == True:
            nodeValues.append(currentNodes[index])
        index = index + 1

    for node in nodeValues:
        currentNodes.remove(node)

print(distances)
        
