import sys


# DFS 로 특정 노드를 방문하고 연결된 모든 노드들도 방문
def dfs(x, y, n, graph, cnt):
    # 주어진 범위를 벗어나는 경우에 즉시 종료
    if x <= -1 or x >= n or y <= -1 or y >= n:
        return False

    # 현재 노드를 아직 방문하지 않았다면
    if graph[x][y] == 1:
        # 장애물의 개수 체크
        cnt.append(1)

        # 해당 노드 방문 처리
        graph[x][y] = 0

        # 상, 하, 좌, 우 재귀 호출
        dfs(x - 1, y, n, graph, cnt)
        dfs(x, y - 1, n, graph, cnt)
        dfs(x + 1, y, n, graph, cnt)
        dfs(x, y + 1, n, graph, cnt)
        return True
    return False


def solution():
    n = int(input())
    cnt = []

    graph = []
    for i in range(n):
        graph.append(list(map(int, input())))


    # 모든 노드(위치)에 대하여 장애물 블록을 만든다.
    result = 0
    result_list = []

    for i in range(n):
        for j in range(n):

            # 현재 위치에서 DFS 수행
            if dfs(i, j, n, graph, cnt):
                result += 1

                # 길이를 통해 장애물의 개수 확인
                result_list.append(len(cnt))
                cnt = []

    # 총 블록의 수 출력
    print(result)

    # 장애물의 수 오름차순
    result_list.sort()
    for i in result_list:
        print(i)


solution()
