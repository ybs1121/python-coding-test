n, m = map(int, input().split())
player_x, player_y, player_view = map(int, input().split())

maps = [list(map(int, input().split())) for _ in range(n)]

visit = [[False for _ in range(m)] for _ in range(n)]


visit[player_x][player_y] = True
# 0 - 북
# 1 - 동
# 2 - 남
# 3 - 서

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 0 - 육지
# 1 - 바다

count = 1 # 현재 자기 위치도 카운트
move = True
while True:
    if move:
        move = False
    else:
        break
    ## 내가 갈 곳을 돌아본다
    for i in range(4):

        player_view -= 1

        if player_view <= 0:
            player_view = 3

        nx = player_x + dx[player_view]
        ny = player_y + dy[player_view]

        if 0 <= nx <= n - 1 and 0 <= ny <= m - 1:
            if visit[nx][ny] == False and maps[nx][ny] == 0:
                ## 가보지 않고 육지이면 간다
                player_x = nx
                player_y = ny
                visit[nx][ny] = True
                move = True
                count += 1
                print(nx,ny ,sep= " ")

print(count)
