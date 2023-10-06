import random
import pygame
import sys

pygame.mixer.init()
pygame.init()

# colors
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
neon_red = (255, 49, 49)
neon_green = (57, 255, 20)
light_red = (246, 194, 194)
r = (237, 50, 50)
lp = (203, 195, 227)

# Gaming Window
screen_width = 800
screen_height = 600
game_window = pygame.display.set_mode((screen_width, screen_height))

#background images
bgimage=pygame.image.load("bg.jpg")
bgimage=pygame.transform.scale(bgimage,(screen_width,screen_height)).convert_alpha()

#Game title
pygame.display.set_caption("Bhayanak Saanp ka Bhookh")

# Clock setting
clock = pygame.time.Clock()

# font
font = pygame.font.SysFont(None, 55)

def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    game_window.blit(screen_text, [x, y])

def plot_snake(game_window, color, snk_list, snake_sizex, snake_sizey):
    for x, y in snk_list:
        pygame.draw.rect(game_window, color, [x, y, snake_sizex, snake_sizey])

def welcome():
    exit_game = False
   
    while not exit_game:
        game_window.fill(lp)
        text_screen("Welcome to the world of Snake", black, 150, 250)
        text_screen("Press space bar to play the Game", black, 140, 290)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.mixer.music.load("background.mp3")
                    pygame.mixer.music.play()
                    gameloop()
    

        pygame.display.update()
        clock.tick(60)

# Game loop
def gameloop():
    # game-specific variables
    exit_game = False
    game_over = False
    init_velocity = 3
    velocity_x = 0
    velocity_y = 0
    velocity_increse=.5 
    snake_x = 45
    snake_y = 45
    snake_sizex = 30 
    snake_sizey = 30  
    with open("hiscore.txt", "r") as f:
        hiscore = f.read()
    food_x = random.randint(50, screen_width/2)
    food_y = random.randint(50, screen_height/2)
    score = 0
    fps = 30
    snk_list = []
    snk_length = 1
    
    aimg=pygame.image.load("apple.png")
    aimg = pygame.transform.scale(aimg, (2*snake_sizex, 2*snake_sizey))
    
    while not exit_game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    gameloop()
                    
                if not game_over:  
                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y = 0
                        pygame.mixer.Sound("ting.mp3").play()
                    
                    if event.key == pygame.K_LEFT:
                        velocity_x = -init_velocity
                        velocity_y = 0
                        pygame.mixer.Sound("ting.mp3").play()
                    
                    if event.key == pygame.K_DOWN:
                        velocity_y = init_velocity
                        velocity_x = 0
                        pygame.mixer.Sound("ting.mp3").play()
                    
                    if event.key == pygame.K_UP:
                        velocity_y = -init_velocity
                        velocity_x = 0
                        pygame.mixer.Sound("ting.mp3").play()
                                            
                    # CHEAT CODE  
                    if event.key == pygame.K_m:
                        score += 10


                        
        
        if not game_over:
            snake_x += velocity_x  
            snake_y += velocity_y  

            if abs(snake_x - food_x) < 20 and abs(snake_y - food_y) < 20:
                pygame.mixer.Sound("beep.mp3").play()
                score += 10
                food_y = random.randint(20, screen_height/2)
                food_x = random.randint(20, screen_width/2)
                snk_length += 5
                if score > int(hiscore):
                    hiscore = score

                init_velocity+= velocity_increse
                   

            game_window.fill(white)
            game_window.blit(bgimage,(0,0))
            text_screen("Score: " + str(score), neon_green, 5, 5)
            text_screen("Highscore: " + str(hiscore), neon_green, 500, 5)
            game_window.blit(aimg, (food_x, food_y))
            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list) > snk_length:
                del snk_list[0]

            # Check for collision with boundaries
            if (snake_x >= screen_width or snake_x < 0 or snake_y >= screen_height or snake_y < 0):
                game_over = True
               
                
                pygame.mixer.Sound("gameover.mp3").play()
             

            # Check for collision with itself
            for i in snk_list[:-1]:
                if i == head:
                    game_over = True
                    
                    pygame.mixer.Sound("gameover.mp3").play()
             

        
        plot_snake(game_window, black, snk_list, snake_sizex, snake_sizey)

        # GAME OVER
        if game_over:
            with open("hiscore.txt", "w") as f:
                f.write(str(hiscore))
            game_window.fill(light_red)
            
            text_screen("Game over!! Press Enter to Continue", red, 100, 250)
            text_screen("Highscore: " + str(hiscore), r, 500, 5)

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        gameloop() 
                    elif event.key == pygame.K_ESCAPE:
                        pygame.quit()  
                        sys.exit()

        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    sys.exit()

welcome()
