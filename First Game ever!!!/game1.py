"Programmed by Antoine BALDO"

import os
import random
import pygame
import sys
import cv2
import time as temps
from pygame import *

def game(NumbEnemy):
    WIN_WIDTH = 800
    WIN_HEIGHT = 640
    HALF_WIDTH = int(WIN_WIDTH / 2)
    HALF_HEIGHT = int(WIN_HEIGHT / 2)

    DISPLAY = (WIN_WIDTH, WIN_HEIGHT)
    DEPTH = 32
    FLAGS = 0

    os.environ['SDL_VIDEO_CENTERED'] = '1'
    ###########################################################################################################
    spritesheet = pygame.image.load("Media/Graphics/rightunicorn.png")

    charactere = Surface((250,175),pygame.SRCALPHA)
    charactere.blit(spritesheet,(-262,0))
    charactere = pygame.transform.scale(charactere, (30*3,25*3))
    unicorn_stay = charactere

    charactere = Surface((265,182),pygame.SRCALPHA)
    charactere.blit(spritesheet,(-1,-1))
    charactere = pygame.transform.scale(charactere, (30*3,25*3))
    unicorn_run = charactere

    charactere = Surface((238,172),pygame.SRCALPHA)
    charactere.blit(spritesheet,(-257,-174))
    charactere = pygame.transform.scale(charactere, (30*3,25*3))
    unicorn_hit = charactere

    charactere = Surface((213,167),pygame.SRCALPHA)
    charactere.blit(spritesheet,(-9,-181))
    charactere = pygame.transform.scale(charactere, (30*3,25*3))
    unicorn_jump = charactere

    charactere = Surface((267,119),pygame.SRCALPHA)
    charactere.blit(spritesheet,(-123,-352))
    charactere = pygame.transform.scale(charactere, (30*3,25*3))
    unicorn_Dead = charactere

    ###########################################################################################################
    spritesheetEvil1 = pygame.image.load("Media/Graphics/Evil1.png")
    #1-2-3-4-5-1
    charactere = Surface((60,60),pygame.SRCALPHA)
    charactere.blit(spritesheetEvil1,(-6,-6))
    charactere = pygame.transform.scale(charactere, (35*2,35*2))
    Evil1_move1 = charactere

    charactere = Surface((50,50),pygame.SRCALPHA)
    charactere.blit(spritesheetEvil1,(-68,-9))
    charactere = pygame.transform.scale(charactere, (35*2,35*2))
    Evil1_move2 = charactere

    charactere = Surface((54,48),pygame.SRCALPHA)
    charactere.blit(spritesheetEvil1,(-130,-12))
    charactere = pygame.transform.scale(charactere, (35*2,35*2))
    Evil1_move3 = charactere

    charactere = Surface((53,44),pygame.SRCALPHA)
    charactere.blit(spritesheetEvil1,(-195,-10))
    charactere = pygame.transform.scale(charactere, (35*2,35*2))
    Evil1_move4 = charactere

    charactere = Surface((48,44),pygame.SRCALPHA)
    charactere.blit(spritesheetEvil1,(-260,-10))
    charactere = pygame.transform.scale(charactere, (35*2,35*2))
    Evil1_move5 = charactere

    charactere = Surface((53,47),pygame.SRCALPHA)
    charactere.blit(spritesheetEvil1,(-259,-137))
    charactere = pygame.transform.scale(charactere, (35*2,35*2))
    Evil1_dead = charactere

    ###########################################################################################################
    spritesheetEvil2 = pygame.image.load("Media/Graphics/Evil2.png")
    #1-2-3-4-5-1
    charactere = Surface((35,35),pygame.SRCALPHA)
    charactere.blit(spritesheetEvil2,(-9,-9))
    charactere = pygame.transform.scale(charactere, (30,30))
    Evil2_move1 = charactere

    charactere = Surface((35,35),pygame.SRCALPHA)
    charactere.blit(spritesheetEvil2,(-61,-11))
    charactere = pygame.transform.scale(charactere, (30,30))
    Evil2_move2 = charactere

    charactere = Surface((35,35),pygame.SRCALPHA)
    charactere.blit(spritesheetEvil2,(-109,-6))
    charactere = pygame.transform.scale(charactere, (30,30))
    Evil2_move3 = charactere

    charactere = Surface((35,35),pygame.SRCALPHA)
    charactere.blit(spritesheetEvil2,(-160,-2))
    charactere = pygame.transform.scale(charactere, (30,30))
    Evil2_move4 = charactere

    charactere = Surface((35,35),pygame.SRCALPHA)
    charactere.blit(spritesheetEvil2,(-210,-8))
    charactere = pygame.transform.scale(charactere, (30,30))
    Evil2_move5 = charactere

    ###########################################################################################################
    spritesheetEvil3 = pygame.image.load("Media/Graphics/Evil3.png")
    #1-2-1-3-1
    charactere = Surface((51,55),pygame.SRCALPHA)
    charactere.blit(spritesheetEvil3,(-58,-6))
    charactere = pygame.transform.scale(charactere, (48*3,50*3))
    Evil3_move1 = charactere

    charactere = Surface((55,55),pygame.SRCALPHA)
    charactere.blit(spritesheetEvil3,(-3,-6))
    charactere = pygame.transform.scale(charactere, (48*3,50*3))
    Evil3_move2 = charactere

    charactere = Surface((55,58),pygame.SRCALPHA)
    charactere.blit(spritesheetEvil3,(-222,-2))
    charactere = pygame.transform.scale(charactere, (48*3,50*3))
    Evil3_move3 = charactere

    ###########################################################################################################
    image_loose = cv2.imread("Media/Graphics/loose.png",0)
    image_win = cv2.imread("Media/Graphics/win.jpg",0)
    ###########################################################################################################
    def main():
        pygame.init()
        screen = pygame.display.set_mode(DISPLAY, FLAGS, DEPTH)
        pygame.display.set_caption("Unicorne Game!")
        timer = pygame.time.Clock()

        up = down = left = right = running = False
        bg = Surface((WIN_WIDTH,WIN_WIDTH))
        bg.convert()
        entities = pygame.sprite.Group()
        enemygroup = pygame.sprite.Group()
        player = Player(32*1, 32*22)

        for i in range (NumbEnemy) :
            enemygroup.add(Evil1(32*random.randint(8,41), 32*random.randint(1,24)))

        platforms = []

        x = y = 0
        level = [
           " PPPPPPPPPPPWPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP",
            "P                                          P",
            "P                                          P",
            "P                                          P",
            "P                     PPPPPP               P",
            "P                                          P",
            "P                                          P",
            "P                                          P",
            "P                                          P",
            "P                                        PPP",
            "P                                          P",
            "P                     PPPPPP               P",
            "P         PPPPPPP                          P",
            "P       PP                                 P",
            "P                                          P",
            "P                       PPPPPPP            P",
            "P                                          P",
            "P                                          P",
            "P   PPPPPPP                                P",
            "P                                          P",
            "P          ppp       PPPPPPPPPPP           P",
            "P      pp                       PP         P",
            "P                                          P",
            "P                                          P",
            "P                                          P",
            "P                                          P",
            "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP",]
        # build the level
        for row in level:
            for col in row:
                if col == "P":
                    p = Platform(x, y)
                    platforms.append(p)
                    entities.add(p)
                if col == "W":
                    w = WinBlock(x, y)
                    platforms.append(w)
                    entities.add(w)
                x += 32
            y += 32
            x = 0

        total_level_width  = len(level[0])*32
        total_level_height = len(level)*32
        camera = Camera(complex_camera, total_level_width, total_level_height)
        entities.add(player)

        while 1:
            timer.tick(60)

            for e in pygame.event.get():
                if e.type == QUIT: raise SystemExit, "QUIT"
                if e.type == KEYDOWN and e.key == K_ESCAPE:
                    raise SystemExit, "ESCAPE"
                if e.type == KEYDOWN and e.key == K_UP:
                    up = True
                if e.type == KEYDOWN and e.key == K_DOWN:
                    down = True
                if e.type == KEYDOWN and e.key == K_LEFT:
                    left = True
                if e.type == KEYDOWN and e.key == K_RIGHT:
                    right = True
                if e.type == KEYDOWN and e.key == K_SPACE:
                    running = True

                if e.type == KEYUP and e.key == K_UP:
                    up = False
                if e.type == KEYUP and e.key == K_DOWN:
                    down = False
                if e.type == KEYUP and e.key == K_RIGHT:
                    right = False
                if e.type == KEYUP and e.key == K_LEFT:
                    left = False

            screen.blit(bg,(0,0))

            camera.update(player)

            # update player, draw everything else
            player.update(up, down, left, right, running, platforms, enemygroup)
            for e in entities:
                screen.blit(e.image, camera.apply(e))
            for e in enemygroup:
                screen.blit(e.image, camera.apply(e))
                e.update(platforms, entities)
            pygame.display.update()

    class Camera(object):
        def __init__(self, camera_func, width, height):
            self.camera_func = camera_func
            self.state = Rect(0, 0, width, height)

        def apply(self, target):
            return target.rect.move(self.state.topleft)

        def update(self, target):
            self.state = self.camera_func(self.state, target.rect)

    def simple_camera(camera, target_rect):
        l, t, _, _ = target_rect
        _, _, w, h = camera
        return Rect(-l+HALF_WIDTH, -t+HALF_HEIGHT, w, h)

    def complex_camera(camera, target_rect):
        l, t, _, _ = target_rect
        _, _, w, h = camera
        l, t, _, _ = -l+HALF_WIDTH, -t+HALF_HEIGHT, w, h

        l = min(0, l)                           # stop scrolling at the left edge
        l = max(-(camera.width-WIN_WIDTH), l)   # stop scrolling at the right edge
        t = max(-(camera.height-WIN_HEIGHT), t) # stop scrolling at the bottom
        t = min(0, t)                           # stop scrolling at the top
        return Rect(l, t, w, h)

    class Entity(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)

    class Player(Entity):
        def __init__(self, x, y):
            Entity.__init__(self)
            self.xvel = 0
            self.yvel = 0
            self.faceright = True
            self.onGround = False
            self.airborne = True
            self.counter = 0
            self.image = unicorn_stay
            self.rect = Rect(x, y, 28*3, 23*3)
            self.lifetotal = ["", "l", "ll", "lll", "llll", "lllll", "llllll", "lllllll", "llllllll", "lllllllll"]
            self.takingdamage = False
            self.attacking = False


        def update(self, up, down, left, right, running, platforms, enemygroup):
            if up:
                # only jump if on the ground
                if self.onGround: self.yvel -= 10
            if down:
                pass
            if running:
                self.xvel = 9
            if left:
                self.xvel = -9
                self.faceright = False
            if right:
                self.xvel = 9
                self.faceright = True
            if not self.onGround:
                # only accelerate with gravity if in the air
                self.yvel += 0.3
                # max falling speed
                if self.yvel > 100: self.yvel = 100
            if not(left or right):
                self.xvel = 0
            if self.yvel < 0 or self.yvel > 1.2 : self.airborne = True
            # increment in x direction
            self.rect.left += self.xvel
            # do x-axis collisions
            self.collide(self.xvel, 0, platforms, enemygroup)
            # increment in y direction
            self.rect.top += self.yvel
            # assuming we're in the air
            self.onGround = False;
            # do y-axis collisions
            self.collide(0, self.yvel, platforms, enemygroup)

            self.animate()

        def collide(self, xvel, yvel, platforms, enemygroup):
            for p in platforms:
                if pygame.sprite.collide_rect(self, p):
                    if isinstance(p, WinBlock):
                        cv2.imshow('GAGNE !!!!',image_win)
                        cv2.waitKey(0)
                        BREAK
                        # pygame.event.post(pygame.event.Event(QUIT))
                    if xvel > 0:
                        self.rect.right = p.rect.left
                    if xvel < 0:
                        self.rect.left = p.rect.right
                    if yvel > 0:
                        self.rect.bottom = p.rect.top
                        self.onGround = True
                        self.airborne = False
                        self.yvel = 0
                    if yvel < 0:
                        self.rect.top = p.rect.bottom
            for e in enemygroup:
                if pygame.sprite.collide_rect(self, e) :
                    dif = self.rect.bottom - e.rect.top
                    if dif <= 13:
                        self.yvel = -8
                    else:
                        cv2.imshow('PERDU !!!!',image_loose)
                        cv2.waitKey(0)
                        pygame.event.post(pygame.event.Event(QUIT))


        def animate(self):
            if self.xvel > 0 or self.xvel < 0 :
                self.walkloop()
                if self.airborne : self.updatecharacter(unicorn_jump)
            else :
                self.updatecharacter(unicorn_stay)
                if self.airborne : self.updatecharacter(unicorn_jump)

        def walkloop(self):
            if self.counter == 5:
                self.updatecharacter(unicorn_run)
            elif self.counter == 10:
                self.updatecharacter(unicorn_stay)
            elif self.counter == 15:
                self.updatecharacter(unicorn_stay)
            elif self.counter == 20:
                self.updatecharacter(unicorn_stay)
            elif self.counter == 25:
                self.updatecharacter(unicorn_run)
                self.counter = 0

            self.counter = self.counter + 1

        def updatecharacter(self, ansurf):
            if not self.faceright: ansurf = pygame.transform.flip(ansurf, True, False)
            self.image = ansurf

    class Evil1(Entity):
        def __init__(self, x, y) :
            Entity.__init__(self)
            alea1 = random.randint(1,2)
            if alea1 == 1 :
                self.xvel = -2
            if alea1 == 2 :
                self.xvel = -3
            self.yvel = 0
            self.onGround = False
            self.destroyed = False
            self.faceright = False
            self.counter = 0
            self.image = Evil1_move1
            self.rect = Rect(x, y, 30*2, 30*2)

        def update(self, platforms, entities):
            if not self.onGround :
                self.yvel += 0.3
                if self.yvel > 100: self.yvel = 100

            self.rect.left += self.xvel
            self.collide(self.xvel, 0, platforms, entities)
            self.rect.top += self.yvel
            self.onGround = False;
            self.collide(0, self.yvel, platforms, entities)

            self.animate()

        def collide(self, xvel, yvel, platforms, entities):
            for p in platforms:
                if pygame.sprite.collide_rect(self, p):
                    if isinstance(p, WinBlock):
                        pygame.event.post(pygame.event.Event(QUIT))
                    if xvel > 0:
                        self.rect.right = p.rect.left
                        self.xvel = -abs(xvel)
                        self.faceright = False
                    if xvel < 0:
                        self.rect.left = p.rect.right
                        self.xvel = abs(xvel)
                        self.faceright = True
                    if yvel > 0:
                        self.rect.bottom = p.rect.top
                        self.onGround = True
                        self.airborne = False
                        self.yvel = 0
                    if yvel < 0:
                        self.rect.top = p.rect.bottom
            for p in entities:
                if pygame.sprite.collide_rect(self, p) :
                    dif = p.rect.bottom - self.rect.top
                    if dif <= 13 :
                        self.destroyed = True
                        self.counter = 0
                        self.xvel = 0
        
        def animate(self):
            if not self.destroyed: 
                self.walkloop()
            else : 
                self.destroyloop()

        def walkloop(self):
            if self.counter == 5:
                self.updatecharacter(Evil1_move1)
            elif self.counter == 10:
                self.updatecharacter(Evil1_move2)
            elif self.counter == 15:
                self.updatecharacter(Evil1_move3)
            elif self.counter == 20:
                self.updatecharacter(Evil1_move4)
            elif self.counter == 25:
                self.updatecharacter(Evil1_move5)
                self.counter = 0
            self.counter = self.counter + 1

        def destroyloop(self):
            if self.counter == 0:
                self.updatecharacter(Evil1_dead)
            elif self.counter == 10: self.kill()
            self.counter = self.counter + 1

        def updatecharacter(self, ansurf):
            if not self.faceright: ansurf = pygame.transform.flip(ansurf, True, False)
            self.image = ansurf

    class Platform(Entity):
        def __init__(self, x, y):
            Entity.__init__(self)
            self.image = pygame.image.load("Media/Graphics/rainbow-block1.png").convert()
            self.rect = Rect(x, y, 32, 32)

        def update(self):
            pass

    class WinBlock(Platform):
        def __init__(self, x, y):
            Platform.__init__(self, x, y)
            self.image = pygame.image.load("Media/Graphics/rainbowwin.png").convert()
            self.rect = Rect(x, y, 32, 32)

    # if __name__ == "__main__":
    main()
# game(0)