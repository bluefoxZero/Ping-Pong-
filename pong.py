import sys, pygame

PADDLE_WIDTH = 50
PADDLE_HEIGHT = 240
BLACK = (0,0,0)
WHITE = (255, 255, 255)
size = SCREEN_WIDTH,SCREEN_HEIGHT = 900, 800

class ball():
    def __init__(self):
        self.x, self.y = SCREEN_WIDTH/2, SCREEN_HEIGHT/2
        self.speed_x = -20
        self.speed_y = -30
        #ball = pygame.image.load("ball.bmp")
        #self.ball = pygame.transform.scale(ball, (100,100))
        #self.ballrect = ball.get_rect()

    def animate(self,player1,player2):
        self.y += self.speed_y
        self.x += self.speed_x

        if self.y <= 0 or self.y + 30> SCREEN_HEIGHT:
            self.speed_y *= -1

        if (self.x <= PADDLE_WIDTH) and (
            self.y > self.get_player_pos(player1)[1]
            and self.y < self.get_player_pos(player1)[1] + PADDLE_HEIGHT):
            self.speed_x *= -1

        elif self.x >= SCREEN_WIDTH - PADDLE_WIDTH and (
            self.y > self.get_player_pos(player2)[1]
            and self.y < self.get_player_pos(player2)[1] + PADDLE_HEIGHT):
            self.speed_x *= -1

        if self.x <= 0:
            player2.score += 1
            self.__init__()

        elif self.x >= SCREEN_WIDTH:
            player1.score += 1
            self.__init__()


    def get_player_pos(self,player):
        return [player.x, player.y]

    def draw(self):
        #screen.blit(self.ball, self.ballrect)
        pygame.draw.rect(screen, WHITE, [self.x, self.y, 30, 30], 0)

class Player1():
    def __init__(self):
        self.x, self.y = 0, SCREEN_HEIGHT/2
        self.speed_y = -30
        self.score = 0

    def animate(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.y += self.speed_y
        if keys[pygame.K_s]:
            self.y -= self.speed_y

        if self.y < 0:
            self.y = 0
        elif self.y + PADDLE_HEIGHT > SCREEN_HEIGHT:
            self.y = SCREEN_HEIGHT - PADDLE_HEIGHT

    def draw(self):
        pygame.draw.rect(screen, WHITE, [self.x, self.y, PADDLE_WIDTH, PADDLE_HEIGHT], 0)

class Player2():
    def __init__(self):
        self.x, self.y = SCREEN_WIDTH - PADDLE_WIDTH, SCREEN_HEIGHT/2
        self.speed_y = -30
        self.score = 0

    def animate(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.y += self.speed_y
        if keys[pygame.K_DOWN]:
            self.y -= self.speed_y

        if self.y < 0:
            self.y = 0
        elif self.y + PADDLE_HEIGHT > SCREEN_HEIGHT:
            self.y = SCREEN_HEIGHT - PADDLE_HEIGHT

    def draw(self):
        pygame.draw.rect(screen, WHITE, [self.x, self.y, PADDLE_WIDTH, PADDLE_HEIGHT], 0)



pygame.init()
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pong")
ball = ball()
player1 = Player1()
player2 = Player2()

clock = pygame.time.Clock()


while True:
    clock.tick(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    ball.animate(player1,player2)
    player1.animate()
    player2.animate()

    screen.fill(BLACK)
    ball.draw()
    player1.draw()
    player2.draw()

    #just at the end of the while
    pygame.display.flip()

pygame.quit()
