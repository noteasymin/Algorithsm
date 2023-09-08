from collections import deque


# 시작도시와 공사중인 도시를 인자로 받아오기
# off라는 이름의 인자에 공사중인 도시를 전달받기. 탐색 과정에서 off를 만나면 건너뛰기

def bfs(start, off):
    # 만약 시작점과 off가 같다면 바로 -1 반환
    if start == off:
        return -1

    # 아니라면 방문 체크를 위한 배열과 큐를 선언
    visited = [0] * (N + 1)
    q = deque([start])

    visited[start] = 1

    # 최단 경로에 대한 정보를 담을 변수를 선언
    # 경로에는 시작점도 포함되므로, 1로 초기화
    step = 1

    while q:
        # step += 1
        step += 1
        # 현재 큐의 길이만큼만 반복해야 최단 경로를 구할 수 있음
        for _ in range(len(q)):
            now = q.popleft()

            # 현재 위치에서 도달할 수 있는 모든 점에 대해 탐색
            # 만약 방문했거나 off 인 경우는 건너뛰어야 함
            for to in graph[now]:
                if visited[to] or to == off:
                    continue

                # 만약 to == E라면 최단 경로를 통해 끝에 도달한 것
                # 이 때, 최단 경로의 길이는 step에 저장되어 있으므로 반환
                if to == E:
                    return step

                # 아니라면 방문체크하고 큐에 추가
                visited[to] = 1
                q.append(to)

            # 탐색 중간에 E를 마주쳤다면 이미 return step을 통해 bfs() 함수 자체가 종료되었을 것
            # 하지만 큐가 빌 때까지 E에 도달하지 못했다면 while문이 종료되고 이 부분이 실행될 것
            # 이는 E로 가는 것이 불가능함을 의미하므로 -1을 반환
    return -1


N, M, S, E = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# 1번 도시부터 N번 도시까지, 각 도시가 공사중일 때
# S번 도시에서 E번 도시까지의 최단 경로를 구해 출력
for i in range(1, N + 1):
    print(bfs(S, i))
