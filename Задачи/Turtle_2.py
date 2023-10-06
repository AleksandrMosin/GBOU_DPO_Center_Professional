n, m = map(int, input().split())
location = [list(map(int, input().split())) for i in range(n)]
cost = [[0] * m for i in range(n)]
road = [[""] * m for i in range(n)]
cost[0][0] = location[0][0]

for X in range(1, m):
    cost[0][X] = cost[0][X - 1] + location[0][X]
    road[0][X] = road[0][X - 1] + 'R'

for Y in range(1, n):
    cost[Y][0] = cost[Y - 1][0] + location[Y][0]
    road[Y][0] = road[Y - 1][0] + 'D'

for Y in range(1, n):
    for X in range(1, m):
        cost[Y][X] = max(cost[Y][X - 1], cost[Y - 1][X]) + location[Y][X]
        if cost[Y][X - 1] > cost[Y - 1][X]:
            road[Y][X] = road[Y][X - 1] + 'R'
        else:
            road[Y][X] = road[Y - 1][X] + 'D'
print(cost[-1][-1])
print(*road[-1][-1])