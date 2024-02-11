import pygame
import random
import datetime  

# Initialize Pygame
pygame.init()

# Screen settings
width = 800
height = 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)

# Block size and snake speed
block_size = 20
speed = 15

# Font and text size
font = pygame.font.SysFont(None, 35)

# Function to draw the snake on the screen
def draw_snake(snake, block_size):
    for segment in snake:
        pygame.draw.rect(screen, green, [segment[0], segment[1], block_size, block_size])

# Function to draw the point on the screen
def draw_point(point):
    pygame.draw.rect(screen, red, [point[0], point[1], block_size, block_size])

# Function to handle the main game loop
def game():
    game_active = True
    points = 0

    while game_active:
        snake = [[width / 2, height / 2]]
        direction = "RIGHT"
        point = [random.randrange(1, (width // block_size)) * block_size,
                 random.randrange(1, (height // block_size)) * block_size]
        start_time = datetime.datetime.now()
        game_over = False

        while not game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT and direction != "RIGHT":
                        direction = "LEFT"
                    elif event.key == pygame.K_RIGHT and direction != "LEFT":
                        direction = "RIGHT"
                    elif event.key == pygame.K_UP and direction != "DOWN":
                        direction = "UP"
                    elif event.key == pygame.K_DOWN and direction != "UP":
                        direction = "DOWN"
                    elif event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        quit()

            new_head = [snake[0][0], snake[0][1]]

            if direction == "LEFT":
                new_head[0] -= block_size
            elif direction == "RIGHT":
                new_head[0] += block_size
            elif direction == "UP":
                new_head[1] -= block_size
            elif direction == "DOWN":
                new_head[1] += block_size

            new_head[0] = new_head[0] % width
            new_head[1] = new_head[1] % height

            snake.insert(0, new_head)

            if snake[0] == point:
                point = [random.randrange(1, (width // block_size)) * block_size,
                         random.randrange(1, (height // block_size)) * block_size]
                points += 1
            else:
                snake.pop()

            for segment in snake[1:]:
                if snake[0] == segment:
                    game_over = True

            screen.fill(black)
            draw_snake(snake, block_size)
            draw_point(point)

            elapsed_time = datetime.datetime.now() - start_time
            time_text = font.render("Time: " + str(elapsed_time.seconds), True, white)
            screen.blit(time_text, (10, 10))

            points_text = font.render("Points: " + str(points), True, white)
            screen.blit(points_text, (10, 50))

            pygame.display.update()
            pygame.time.Clock().tick(speed)


        points = 0
        
    pygame.quit()
    quit()

# Start the game
game()
