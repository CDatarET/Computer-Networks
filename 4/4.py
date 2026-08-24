n = 4
inf = 999

cost = []
dist = []
nextHop = []
for i in range(n):
    a = []
    b = []
    c = []
    for j in range(n):
        a.append(0)
        b.append(0)
        c.append(0)
    
    cost.append(a)
    dist.append(b)
    nextHop.append(c)

print("Enter enter values of matrix-")
for i in range(n):
    for j in range(n):
        t = int(input())
        cost[i][j] = t

for i in range(n):
    for j in range(n):
        dist[i][j] = cost[i][j]

        if i == j:
            nextHop[i][j] = i
        elif cost[i][j] != inf:
            nextHop[i][j] = j
        else:
            nextHop[i][j] = -1
while True:
    updated = 0
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if dist[i][k] != inf and dist[k][j] != inf and dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    nextHop[i][j] = nextHop[i][k]
                    updated = 1
    if updated == 0:
        break

routers = ['A', 'B', 'C', 'D']
for i in range(n):
    print("\nRouting table for Router " + str(routers[i]))
    print("Destination\tCost\tNext Hop")

    for j in range(n):
        print(str(routers[j]) + "\t\t" + str(dist[i][j]) + "\t" + str(routers[nextHop[i][j]]))