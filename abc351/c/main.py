n = int(input())
a = list(map(int, input().split(" ")))


ball_num = 1
balls = [a[0]]

for i in range(1, n):
    add_ball = a[i]
    ball_num += 1
    left_ball = balls[-1]
    while add_ball == left_ball:
        balls.pop()
        add_ball += 1
        ball_num -= 1
        if len(balls) == 0:
            break
        left_ball = balls[-1]
    balls.append(add_ball)

print(ball_num)