# AIoT
---
## AIoT 로봇 스마트융합 제조 실무
---
## 파이썬을 이용하여 만든 벽돌깨기 게임
import pygame
import random

# 초기화
pygame.init()

# 화면 설정
WIDTH, HEIGHT = 600, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("벽돌깨기 게임")

# 색상
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BRICK_COLOR = (200, 50, 50)

# 공 설정
ball_radius = 10
ball_speed = [4, -4]
ball = pygame.Rect(WIDTH // 2, HEIGHT // 2, ball_radius * 2, ball_radius * 2)

# 패들 설정
paddle_width = 100
paddle_height = 15
paddle = pygame.Rect(WIDTH // 2 - paddle_width // 2, HEIGHT - 50, paddle_width, paddle_height)
paddle_speed = 6

# 벽돌 설정
bricks = []
brick_rows = 5
brick_cols = 10
brick_width = WIDTH // brick_cols
brick_height = 30

for row in range(brick_rows):
    for col in range(brick_cols):
        brick = pygame.Rect(col * brick_width, row * brick_height + 50, brick_width - 2, brick_height - 2)
        bricks.append(brick)

# 게임 루프
clock = pygame.time.Clock()
running = True

while running:
    clock.tick(60)  # FPS 제한
    screen.fill(BLACK)

    # 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 키 입력 처리
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle.left > 0:
        paddle.x -= paddle_speed
    if keys[pygame.K_RIGHT] and paddle.right < WIDTH:
        paddle.x += paddle_speed

    # 공 움직이기
    ball.x += ball_speed[0]
    ball.y += ball_speed[1]

    # 벽 충돌
    if ball.left <= 0 or ball.right >= WIDTH:
        ball_speed[0] = -ball_speed[0]
    if ball.top <= 0:
        ball_speed[1] = -ball_speed[1]

    # 패들과 충돌
    if ball.colliderect(paddle):
        ball_speed[1] = -ball_speed[1]

    # 벽돌과 충돌
    hit_index = ball.collidelist(bricks)
    if hit_index != -1:
        del bricks[hit_index]
        ball_speed[1] = -ball_speed[1]

    # 바닥으로 떨어짐 (게임 오버)
    if ball.bottom >= HEIGHT:
        print("Game Over!")
        running = False

    # 그리기
    pygame.draw.ellipse(screen, WHITE, ball)
    pygame.draw.rect(screen, WHITE, paddle)
    for brick in bricks:
        pygame.draw.rect(screen, BRICK_COLOR, brick)

    pygame.display.flip()

pygame.quit()
