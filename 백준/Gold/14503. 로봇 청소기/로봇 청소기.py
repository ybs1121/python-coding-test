# N, M = map(int, input().split())
# r, c, d = map(int, input().split())
# # 0 북쪽
# # 1 동쪽
# # 2 남쪽
# # 3 서쪽
# nx = [-1, 0, 1, 0]
# ny = [0, 1, 0, -1]
#
# back_step_nx = [1, 0, -1, 0]
# back_step_ny = [0, -1, 0, 1]
#
# maps = []
# for i in range(N):
#     row = list(map(int, input().split()))
#     maps.append(row)
# clean_map = [[False for j in range(M)] for i in range(N)]
#
# clean_area_cnt = 0
#
# while True:
#     # 청소 가능?
#
#     if maps[r][c] == 0:
#         if not clean_map[r][c]:
#             clean_area_cnt += 1
#             clean_map[r][c] = True
#
#     possible_clean = False
#     next_watch = d + 1
#     for i in range(4):
#         if next_watch == 4:
#             next_watch = 0
#
#         dx = r + nx[next_watch]
#         dy = c + ny[next_watch]
#
#         if 0 <= dx < N and 0 <= dy < M:
#             if maps[dx][dy] == 0 and not clean_map[dx][dy]:
#                 r = dx
#                 c = dy
#                 d = next_watch
#                 possible_clean = True
#                 break
#         next_watch += 1
#
#     if possible_clean:
#         continue
#
#     # 여기 까지 오면 주변에 청소할 곳이 없습니다.
#     # 현재 바라 보는 기준으로 뒤로 한칸 간다.
#
#     back_dx = r + back_step_nx[d]
#     back_dy = c + back_step_ny[d]
#
#     if 0 <= back_dx < N and 0 <= back_dy < M and maps[back_dx][back_dy] != 1:
#         r = back_dx
#         c = back_dy
#         continue
#     break
#
# print(clean_area_cnt)


## 북, 동, 하, 서 ( 시계방향 )
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

n, m = map(int, input().split())
r, c, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
## 방문 쳌
visited = [[0]*m for _ in range(n)]

## 시작지 방문쳌 and 카운트!
visited[r][c] = 1
cnt = 1

while True:
    flag = 0            ## 아직 아무것도 청소 안했음!
    for _ in range(4):  ## 4방향을 돈다!
        d = (d+3) % 4   ## 왼쪽방향으로 한 칸 돌린다! 중요!!!!!1
        nr = r + dr[d]
        nc = c + dc[d]

        ## 범위 안에 들고, 빈 칸이고, 청소할 수 있다면!
        ## 들려서 청소하고, 카운트하고, 현재 위치를 갱신하고, flag 변경!
        if 0 <= nr < n and 0 <= nc < m and arr[nr][nc] == 0:
            if visited[nr][nc] == 0:
                visited[nr][nc] = 1
                cnt += 1
                r = nr
                c = nc
                flag = 1        ## 청소 했다는 뜻
                break

    if flag == 0:               ## 위의 for문에 들어가지 못했을 때
        ## 즉 네 방향 모두 청소를 할 수 없을 때
        ## 후진 했을 때 벽이면 break
        ## 만약 뒤가 벽이 아니라면! 그 위치를 다시 갱신!!!
        if arr[r-dr[d]][c-dc[d]] == 1:
            print(cnt)
            break
        else:
            r, c = r-dr[d], c-dc[d]