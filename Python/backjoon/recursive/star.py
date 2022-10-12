def draw_star(n):
    global Map
    
    if n == 3:
        Map[0][:3] = Map[2][:3] = [1]*3
        Map[1][:3] = [1,0,1]
        print(Map)

N = int(input())

Map = [[0 for i in range(N)] for i in range(N)]

draw_star(3)
