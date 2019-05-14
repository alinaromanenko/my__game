import pygame
from contracts import contract


class Man():
    def __init__(self):
        self.x = 10
        self.y = 300

    @contract()
    def draw(self, win, side, line_y):
        """
        :type side: int, =1 | =2
        :type line_y: int, >=50, <=250
        """
        if side == 1:
            win.blit(pygame.image.load('images/man/0.gif'), (self.x, self.y))
            pygame.display.update()
            for image in range(1, 4):
                win.blit(pygame.image.load('images/bg.jpg'), (0, 0))
                pygame.draw.line(win, (255, 255, 255), (40, 250), (40, line_y), 10)
                win.blit(pygame.image.load('images/man/' + str(image) + '.gif'), (self.x, self.y))
                pygame.display.update()
        if side == 2:
            win.blit(pygame.image.load('images/man/6.gif'), (self.x, self.y))
            pygame.display.update()
            for image in range(7, 10):
                win.blit(pygame.image.load('images/bg.jpg'), (0, 0))
                pygame.draw.line(win, (255, 255, 255), (40, 250), (40, line_y), 10)
                win.blit(pygame.image.load('images/man/' + str(image) + '.gif'), (self.x, self.y))
                pygame.display.update()


class Projectile():
    @contract()
    def __init__(self, score, y):
        """
        :type score: int, >=0, <=100
        :type y: int, <=420
        """
        self.score = score
        self.y = y

    @contract()
    def draw(self, step, win):
        """
        :type step: int, >=30, <=130
        """
        if step in range(self.score // 2 + 30):
            win.blit(pygame.image.load('images/man/ball.gif'), (step * 6.7, self.y - 5))
            self.y -= 5
            pygame.display.update()
        if step in range(self.score // 2 + 30, self.score + 30):
            win.blit(pygame.image.load('images/man/ball.gif'), (step * 6.7, self.y + 5))
            self.y += 5
            pygame.display.update()
        return self.y


@contract()
def winning(score, win, y_fixed):
    """
    :type score: int, >=0, <=100
    #:type win: pygame.Surface
    :type y_fixed: int, >=40, <=250
    :rtype: bool
    """
    pygame.init()
    y_ = 420
    for step in range(score):
        pygame.draw.line(win, (255, 255, 255), (40, 250), (40, y_fixed), 10)
        win.blit(pygame.image.load('images/man/without_ball.gif'), (10, 300))
        font_ = pygame.font.SysFont('Arial', 15)
        t = font_.render(str(score), True, (255, 255, 255))
        win.blit(t, (10, 10))
        y_ = Projectile(score, y_).draw(step + 30, win)
        win.blit(pygame.image.load('images/bg.jpg'), (0, 0))
    pygame.time.wait(2000)
    score_f = pygame.font.SysFont('Arial', 150)
    score_t = score_f.render('Ваш счёт: ' + str(score), True, (255, 255, 255))
    win.blit(score_t, (150, 200))
    pygame.display.update()
    pygame.time.wait(3000)
    f = pygame.font.SysFont('Arial', 120)
    win.blit(pygame.image.load('images/bg.png'), (0, 0))
    pygame.mixer.music.stop()
    if score > 80:
        pygame.mixer.music.load("music/win.mp3")
        pygame.mixer.music.play()
        text = f.render('Победа!', True, (255, 255, 255))
    else:
        text = f.render('Вы проиграли:(', True, (255, 255, 255))
    win.blit(text, (150, 200))
    pygame.display.update()
    pygame.time.wait(3000)
    return False


@contract()
def pic(picture, win):
    """
    :type picture: str
    """
    bg = pygame.image.load('images/bg.jpg')
    win.blit(bg, (0, 0))
    win.blit(pygame.image.load('images/man/' + picture + '.gif'), (10, 300))


def main():
    pressed = 0
    win = pygame.display.set_mode((960, 540))
    pygame.display.set_caption("Sportsman")
    pygame.mixer.init()
    pygame.mixer.music.set_volume(0.9)
    pygame.mixer.music.load("music/360.mp3")
    pygame.mixer.music.play()
    pygame.init()
    print(type(win))
    y_fixed = 0
    y = 250
    run = True
    man = Man()
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        if y_fixed != 0:
            if 250 - y_fixed > 200:
                score = 100
            else:
                score = (250 - y_fixed) // 2
            run = winning(score, win, y_fixed)
        else:

            keys = pygame.key.get_pressed()
            if keys[pygame.K_a] and y > 50 and pressed != 1:
                pressed = 1
                man.draw(win, pressed, y)
                y -= 5
            elif keys[pygame.K_d] and y > 50 and pressed != 2:
                pressed = 2
                man.draw(win, pressed, y)
                y -= 5
            elif keys[pygame.K_w]:
                pygame.draw.line(win, (255, 255, 255), (40, 250), (40, y), 10)
                y_fixed = y
            else:
                if y == 250:
                    pic('steal', win)
                else:
                    if pressed == 1:
                        pic('6', win)

                    elif pressed == 2:
                        pic('9', win)

                pygame.display.update()
                if y < 250:
                    y += 1

            pygame.draw.line(win, (255, 255, 255), (40, 250), (40, y), 10)
            pygame.display.update()


if __name__ == '__main__':
    main()
